import para
import coeff

use_data_num = 50
v = 0
alpha = 0
wing = 1.0

path = './data_file' + '/prop_thrust'  + '/single_all(main1400)/'

print('%d' % (v))
front = para.para_calc1(path + 'front.out','Front',use_data_num)
main = para.para_calc1(path + 'main.out','Main',use_data_num)
left = para.para_calc1(path + 'left.out','Left',use_data_num)
right = para.para_calc1(path + 'right.out','Rightß',use_data_num)
# drag = para.para_calc1(path + 'drag.out','Drag',use_data_num)
# lift = para.para_calc1(path + 'lift.out','Lift',use_data_num)
# moment = para.para_calc1(path + 'moment.out','Moment',use_data_num)

# coeff.coeff_calc(drag,lift,moment,v)

# path = './data_file' + '/23SD2-FW'  + '/no-slim/alpha' + str(alpha) + '/'

# path_parts = 'body_nose'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,2)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,2)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,2)

# path_parts = 'left_wing'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,3)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,3)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,3)

# path_parts = 'right_wing'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,4)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,4)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,4)

# path_parts = 'left_tank'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,5)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,5)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,5)

# path_parts = 'right_tank'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,6)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,6)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,6)

# path_parts = 'left_leg'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,7)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,7)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,7)

# path_parts = 'right_leg'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,8)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,8)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,8)

# path_parts = 'front_leg'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,9)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,9)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,9)

# path_parts = 'left_fin'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,10)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,10)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,10)

# path_parts = 'right_fin'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,11)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,11)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,11)

# path_parts = 'front_frame'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,12)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,12)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,12)

# path_parts = 'back_frame'
# print('%s' % (path_parts))
# drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,13)
# lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,13)
# moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,13)

# # path_parts = 'left_wing_tank_connect'
# # print('%s' % (path_parts))
# # drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,14)
# # lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,14)
# # moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,14)

# # path_parts = 'right_wing_tank_connect'
# # print('%s' % (path_parts))
# # drag = para.para_calc(path + path_parts + '_drag.out','Drag',use_data_num, wing, alpha,15)
# # lift = para.para_calc(path + path_parts + '_lift.out','Lift',use_data_num, wing, alpha,15)
# # moment = para.para_calc(path + path_parts + '_moment.out','Moment',use_data_num, wing, alpha,15)