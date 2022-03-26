# python -u tools/train.py \
#     configs_fdy/exps/fcos/20220103_fcos_center-normbbox-centeronreg-giou_r50_caffe_fpn_gn-head_dcn_1x_coco.py \
#     --gpus 1 \
#     --work-dir work_dirs/20220103_fcos_center_dcn 

# python -u tools/train.py \
#     configs_fdy/exps/fcos/20220313_fcos_center-normbbox-centeronreg-giou_r50_caffe_fpn_gn-head_dcn_1x_voc.py \
#     --gpus 1 \
#     --work-dir work_dirs/20220313_fcos_center_dcn_voc

python -u tools/train.py \
    configs_fdy/exps/fcos/20220324_fcos_center-normbbox-centeronreg-giou_r50_caffe_fpn_gn-head_1x_voc.py \
    --gpus 1 \
    --work-dir work_dirs/20220324_fcos_center_voc
