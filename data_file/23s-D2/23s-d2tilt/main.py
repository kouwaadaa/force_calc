import para

use_data_num = 50
v = 5
alpha = 0
tilt = 10

path = './data_file' + '/tilt' + str(tilt) + '/wind' + str(v) + 'alpha' + str(alpha)

print('tilt=%d' % (tilt))
print('v=%d' % (v))
print('alpha=%d' % (alpha))

lift   = para.para_calc(path + '/lift_body.out',use_data_num,tilt,v,alpha,3)
drag   = para.para_calc(path + '/drag.out',use_data_num,tilt,v,alpha,4)
moment = para.para_calc(path + '/moment.out',use_data_num,tilt,v,alpha,5)
front  = para.para_calc(path + '/thrust_front.out',use_data_num,tilt,v,alpha,7)
main   = para.para_calc(path + '/thrustmain.out',use_data_num,tilt,v,alpha,6)
left   = para.para_calc(path + '/thrust_left.out',use_data_num,tilt,v,alpha,8)
right  = para.para_calc(path + '/thrust_right.out',use_data_num,tilt,v,alpha,9)

#renew 
#sin cos import
para.renew(tilt,v,alpha)