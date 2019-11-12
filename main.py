import para
import coeff

use_data_num = 100
v = 28
alpha = 4
wing = 1.5

# path = './data_file/wingOnly/wing_withhole4/'

# drag = para.para_calc1(path + 'report-file-0.out','Drag',use_data_num)
# lift = para.para_calc1(path + 'report-file-1.out','Lift',use_data_num)
# moment = para.para_calc1(path + 'report-file-2.out','Moment',use_data_num)

# coeff.coeff_calc(drag,lift,moment,v)

path = './data_file' + '/hole_original'  + '/wing'+ str(wing) +'/alpha' + str(alpha) + '/'

path_parts = 'body_nose'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,2)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,2)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,2)

path_parts = 'left_wing'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,3)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,3)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,3)

path_parts = 'right_wing'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,4)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,4)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,4)

path_parts = 'left_tank'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,5)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,5)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,5)

path_parts = 'right_tank'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,6)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,6)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,6)

path_parts = 'left_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,7)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,7)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,7)

path_parts = 'right_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,8)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,8)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,8)

path_parts = 'front_leg'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,9)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,9)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,9)

path_parts = 'left_fin'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,10)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,10)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,10)

path_parts = 'right_fin'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,11)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,11)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,11)

path_parts = 'front_frame'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,12)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,12)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,12)

path_parts = 'back_frame'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,13)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,13)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,13)

path_parts = 'left_wing_tank_connect'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,14)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,14)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,14)

path_parts = 'right_wing_tank_connect'
print('%s' % (path_parts))
drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,15)
lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,15)
moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,15)