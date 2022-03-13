_base_ = ['../../datasets/voc0712.py', '../../default_runtime.py']
model = dict(
    type='FCOS',
    backbone=dict(type='ResNet',
                  depth=50,
                  num_stages=4,
                  out_indices=(0, 1, 2, 3),
                  frozen_stages=1,
                  norm_cfg=dict(type='BN', requires_grad=False),
                  norm_eval=True,
                  style='caffe',
                  dcn=dict(type='DCNv2', deform_groups=1, fallback_on_stride=False),
                  stage_with_dcn=(False, True, True, True),
                  init_cfg=dict(type='Pretrained', checkpoint='open-mmlab://detectron2/resnet50_caffe')
                  # checkpoint='checkpoints/resnet50_msra-5891d200.pth')
                  ),
    neck=dict(
        type='FPN',
        in_channels=[256, 512, 1024, 2048],
        out_channels=256,
        start_level=1,
        add_extra_convs='on_output',  # use P5
        num_outs=5,
        relu_before_extra_convs=True),
    bbox_head=dict(type='FCOSHead',
                   num_classes=20,
                   in_channels=256,
                   stacked_convs=4,
                   feat_channels=256,
                   strides=[8, 16, 32, 64, 128],
                   loss_cls=dict(type='FocalLoss', use_sigmoid=True, gamma=2.0, alpha=0.25, loss_weight=1.0),
                   norm_on_bbox=True,
                   centerness_on_reg=True,
                   dcn_on_last_conv=True,
                   center_sampling=True,
                   conv_bias=True,
                   loss_bbox=dict(type='GIoULoss', loss_weight=1.0),
                   loss_centerness=dict(type='CrossEntropyLoss', use_sigmoid=True, loss_weight=1.0)),
    # training and testing settings
    train_cfg=dict(assigner=dict(type='MaxIoUAssigner',
                                 pos_iou_thr=0.5,
                                 neg_iou_thr=0.4,
                                 min_pos_iou=0,
                                 ignore_iof_thr=-1),
                   allowed_border=-1,
                   pos_weight=-1,
                   debug=False),
    test_cfg=dict(nms_pre=1000,
                  min_bbox_size=0,
                  score_thr=0.05,
                  nms=dict(type='nms', iou_threshold=0.6),
                  max_per_img=100))

# dataset settings
data = dict(samples_per_gpu=4, workers_per_gpu=3)

# optimizer
optimizer = dict(type='SGD',
                 lr=0.01,
                 momentum=0.9,
                 weight_decay=0.0001,
                 paramwise_cfg=dict(bias_lr_mult=2., bias_decay_mult=0.))
optimizer_config = dict(grad_clip=None)

# learning policy
lr_config = dict(policy='step', warmup='linear', warmup_iters=500, warmup_ratio=1.0 / 3, step=[3])
runner = dict(type='EpochBasedRunner', max_epochs=4)

fp16 = dict(loss_scale=512.)