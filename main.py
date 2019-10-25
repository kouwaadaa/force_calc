import para
import coeff

use_data_num = 300
v = 28

# path = './data_file/wing_withhole4/'

# drag = para.para_calc(path + 'report-file-0.out','Drag',use_data_num)
# lift = para.para_calc(path + 'report-file-1.out','Lift',use_data_num)
# moment = para.para_calc(path + 'report-file-2.out','Moment',use_data_num)

# coeff.coeff_calc(drag,lift,moment,v)

path = './data_file/FW_wingwide1.5_alpha4/'

path_parts = 'body_nose'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'left_wing'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'right_wing'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'left_tank'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'right_tank'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'left_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'right_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'front_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'left_fin'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'right_fin'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'front_frame'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'back_frame'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'left_wing_tank_connect'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)

path_parts = 'right_wing_tank_connect'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num)