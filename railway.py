import os
import cv2
import numpy as np

path = "./meter_reading_images/"
bill_data = [file for file in os.listdir(path) if file.endswith('.png')]
print(sorted(bill_data))


def railway_bill(img_path, debug=True):
    print(img_path)

    ig_o = cv2.imread(path + img_path)
    ig = cv2.cvtColor(ig_o, cv2.COLOR_BGR2HSV)

    roi_lower = np.array([40, 25, 0])
    roi_upper = np.array([80, 255, 255])

    mask = cv2.inRange(ig, roi_lower, roi_upper)

    ig = cv2.bitwise_and(ig_o, ig_o, mask=mask)     # Bitwise-AND mask and original image

    # Find contours
    image, contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cntrs = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

    for cnt in cntrs:
        (x, y, w, h) = cv2.boundingRect(cnt)
        wbuffer = 0.75 * w
        hbuffer = 0.1 * h
        ig_ext = ig_o[y:y + h + int(hbuffer), x:x + w + int(wbuffer)]

        ig_ext_gray = cv2.cvtColor(ig_ext, cv2.COLOR_BGR2GRAY)
        ig_ext_pp = cv2.adaptiveThreshold(ig_ext_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,
                                              199, 5)
        ig_ext_pp = cv2.medianBlur(ig_ext_pp, 13)
        cv2.rectangle(ig_o, (x, y), (x + w + int(wbuffer), y + h + int(hbuffer)), (255, 0, 255), 10)
        break

    if debug:
        cv2.imwrite('./output/meter_disp_ext/' + img_path.split('.')[0] + '_ext.png', ig_ext)
        cv2.imwrite('./output/mask/' + img_path.split('.')[0] + '_mask.png', mask)
        cv2.imwrite('./output/meter_disp_bb/' + img_path.split('.')[0] + '_bb.png', ig_o)
        cv2.imwrite('./output/meter_disp_ext_pp/' + img_path.split('.')[0] + '_pp.png', ig_ext_pp)
    print(img_path + 'DONE')


for irctc_bill in bill_data:
    railway_bill(irctc_bill)