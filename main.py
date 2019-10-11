import para
import coeff

use_data_num = 300
v = 28

#path = './data_file/FW_alpha=4/'

#drag = para.para_calc(path + 'report-file-0.out','Drag',use_data_num)
#lift = para.para_calc(path + 'report-file-1.out','Lift',use_data_num)
#moment = para.para_calc(path + 'report-file-2.out','Moment',use_data_num)

#coeff.coeff_calc(drag,lift,moment,v)

path = './data_file/FW_alpha=4_separate/body_nose_'
drag = para.para_calc(path + 'drag.out','Drag',use_data_num)
lift = para.para_calc(path + 'lift.out','Lift',use_data_num)
moment = para.para_calc(path + 'moment.out','Moment',use_data_num)

path = './data_file/FW_alpha=4_separate/left_wing_'
drag = para.para_calc(path + 'drag.out','Drag',use_data_num)
lift = para.para_calc(path + 'lift.out','Lift',use_data_num)
moment = para.para_calc(path + 'moment.out','Moment',use_data_num)

path = './data_file/FW_alpha=4_separate/right_wing_'
drag = para.para_calc(path + 'drag.out','Drag',use_data_num)
lift = para.para_calc(path + 'lift.out','Lift',use_data_num)
moment = para.para_calc(path + 'moment.out','Moment',use_data_num)
