build_time = [40.30965518951416, 13.638967275619507, 18.678813457489014, 14.204166173934937, 24.334273099899292,
              36.29874610900879, 40.283761739730835, 33.21649742126465, 35.8663375377655, 32.55244016647339,
              17.654622554779053, 20.928698539733887, 20.49583387374878, 21.205034732818604, 13.284992694854736,
              14.028726816177368, 14.21750545501709, 40.38567280769348, 23.33819031715393, 1.5455362796783447,
              2.6558480262756348, 2.388890027999878, 4.195888996124268, 1.4770805835723877, 2.536942481994629,
              0.04620671272277832, 0.5170962810516357, 0.7530477046966553, 0.6165473461151123, 1.3530480861663818,
              0.4879617691040039, 0.661461591720581, 0.6423344612121582, 1.6096899509429932, 7.3663105964660645,
              3.1115646362304688, 6.835530996322632, 2.9265997409820557, 6.73129415512085, 4.148857116699219,
              6.373552560806274, 3.063481330871582, 4.743720769882202, 0.6669189929962158, 0.008393287658691406,
              0.00886082649230957, 0.008518457412719727, 0.4210662841796875, 0.34379124641418457, 0.4601116180419922,
              0.42752599716186523, 0.4169039726257324, 0.9586045742034912, 0.42990541458129883, 0.3910202980041504,
              0.34232115745544434, 0.3224952220916748, 0.3056526184082031, 0.3557755947113037]

test_indexes = [31,16,36,37,4,25,8,23,12,32,39,47,46,20,40,1,10,24,34,51]
total = 0
for test_index in test_indexes:
    total += build_time[test_index]
    print(total)