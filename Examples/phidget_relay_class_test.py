import phidgets_relay_class as relay
import time

print(f'Starting relay init ')
brd_ser_nums = [439515, 449740, 449901, 439525]
brd1 = relay.phidget_relay_class(brd_ser_nums[0])
brd2 = relay.phidget_relay_class(brd_ser_nums[1])
brd3 = relay.phidget_relay_class(brd_ser_nums[2])
brd4 = relay.phidget_relay_class(brd_ser_nums[3])
# reset all relay blocks
brd1.relay_reset_all()
brd2.relay_reset_all()
brd3.relay_reset_all()
brd4.relay_reset_all()


def relay_FR_HA(sing_gnd, pwr):
    relay_sensor(brd1, 0, brd2, 0, sing_gnd, pwr)


def relay_FL_HA(sing_gnd, pwr):
    relay_sensor(brd1, 1, brd2, 1, sing_gnd, pwr)


def relay_RR_HA(sing_gnd, pwr):
    relay_sensor(brd1, 2, brd2, 2, sing_gnd, pwr)


def relay_RL_HA(sing_gnd, pwr):
    relay_sensor(brd1, 3, brd2, 3, sing_gnd, pwr)


def relay_FR_HEIGHT(sing_gnd, pwr):
    relay_sensor(brd1, 4, brd2, 4, sing_gnd, pwr)


def relay_FL_HEIGHT(sing_gnd, pwr):
    relay_sensor(brd1, 5, brd2, 5, sing_gnd, pwr)


def relay_RR_HEIGHT(sing_gnd, pwr):
    relay_sensor(brd1, 6, brd2, 6, sing_gnd, pwr)


def relay_RL_HEIGHT(sing_gnd, pwr):
    relay_sensor(brd1, 7, brd2, 7, sing_gnd, pwr)


def relay_AIR_PRESS(sing_gnd, pwr):
    relay_sensor(brd3, 0, brd3, 1, sing_gnd, pwr)

def relay_uprlata(sing_gnd, pwr):
    brd4.relay_switch(3, sing_gnd)

def relay_lwrlata(sing_gnd, pwr):
    brd4.relay_switch(2, sing_gnd)

def relay_lower_sig(state):
    brd3.relay_switch(2, state)


def relay_ris_sig(state):
    brd3.relay_switch(3, state)


def relay_dig_in3(state):
    brd3.relay_switch(4, state)


def relay_dig_in4(state):
    brd3.relay_switch(5, state)


def relay_air_sus_cont(state):
    brd3.relay_switch(6, state)


def relay_ign_in(state):
    brd3.relay_switch(7, state)




def relay_sensor_source_supply(state):
    brd4.relay_switch(1, state)


def relay_group1_switch(state):
    relay_air_sus_cont(state)
    relay_lower_sig(state)
    relay_ris_sig(state)
    relay_dig_in3(state)
    relay_dig_in4(state)
    relay_AIR_PRESS(state, 0)


def relay_group2_switch(state):
    relay_ign_in(state)
    relay_AIR_PRESS(state, 0)


def relay_group3_switch(state):
    relay_FR_HA(state, 0)
    relay_FL_HA(state, 0)
    relay_RR_HA(state, 0)
    relay_RL_HA(state, 0)

    relay_FR_HEIGHT(state, 0)
    relay_FL_HEIGHT(state, 0)
    relay_RR_HEIGHT(state, 0)
    relay_RL_HEIGHT(state, 0)

    relay_AIR_PRESS(state, 0)

    relay_sensor_source_supply(state)


def relay_power(wire_name, state=0):
    if wire_name.lower() == "all":
        brd4.relay_switch(4, state) # V_bat_A
        brd4.relay_switch(5, state) # V_BAT_B
        brd4.relay_switch(6, state) # V_BAT_C
        brd4.relay_switch(7, state) #power supply connect powet rail
    elif wire_name.lower() == "p_vbat_a":
        brd4.relay_switch(4, state)
        brd4.relay_switch(7, state)
    elif wire_name.lower() == "p_vbat_b":
        brd4.relay_switch(5, state)
        brd4.relay_switch(7, state)
    elif wire_name.lower() == "p_vbat_c":
        brd4.relay_switch(6, state)
        brd4.relay_switch(7, state)
    elif wire_name.lower() == "all_on":
        brd4.relay_switch(4, 1)
        brd4.relay_switch(5, 1)
        brd4.relay_switch(6, 1)
        brd4.relay_switch(7, 1)
    elif wire_name.lower() == "all_off":
        brd4.relay_switch(7, 0)
        brd4.relay_switch(4, 0)
        brd4.relay_switch(5, 0)
        brd4.relay_switch(6, 0)
    elif wire_name.lower() == "p_vbat_a_only":
        #print(wire_name)
        brd4.relay_switch(4, 1)
        brd4.relay_switch(5, 1)
        brd4.relay_switch(6, 1)
        brd4.relay_switch(7, 1)
        delay()
        brd4.relay_switch(5, 0)  # V_BAT_B
        brd4.relay_switch(6, 0)  # V_BAT_C
        delay()
    elif wire_name.lower() == "p_vbat_b_only":
        #print(wire_name)
        brd4.relay_switch(4, 1)
        brd4.relay_switch(5, 1)
        brd4.relay_switch(6, 1)
        brd4.relay_switch(7, 1)
        delay()
        brd4.relay_switch(4, 0)  # V_bat_A
        brd4.relay_switch(6, 0)  # V_BAT_C
        delay()
    elif wire_name.lower() == "p_vbat_c_only":
        #print(wire_name)
        brd4.relay_switch(4, 1)
        brd4.relay_switch(5, 1)
        brd4.relay_switch(6, 1)
        brd4.relay_switch(7, 1)
        delay()
        brd4.relay_switch(4, 0)  # V_bat_A
        brd4.relay_switch(5, 0)  # V_BAT_B
        delay()


    else:
        print(f"Function: relay_power() Wrong signal name: {wire_name}, state: {state}")
        print("Available: all, p_vbat_a, p_vbat_b, p_vbat_c, all_on, all_off, p_vbat_a_only, p_vbat_b_only, p_vbat_c_only")


def relay_dmm(pwr_sensor):
    # state = 0 - dmm connected to 5V sensor power bus
    # state = 1 - dmm connected to sensor input bus
    brd4.relay_switch(0, pwr_sensor)


def relay_sensor_source_supply(state):
    brd4.relay_switch(1, state)

if __name__ == "__main__":
    try:
        # relay_power("all_on")
        # relay_sensor_source_supply(1)
        # while 1:
        #     print("On")
        #     relay_group1_switch(1)
        #     time.sleep(5)
        #     print("Off")
        #     relay_group1_switch(0)
        #     time.sleep(5)
        # print("start self test ")
        # # print("brd1")
        # # brd1.relay_self_test()
        # # print("brd2")
        # # brd2.relay_self_test()
        # # print("brd3")
        # # brd3.relay_self_test()
        # print("brd4")
        # brd4.relay_self_test()

        sensor_5VON_volt = [["FR_HA_5V", 0, relay_FR_HA],
                            ["FL_HA_5V", 0, relay_FL_HA],
                            ["RR_HA_5V", 0, relay_RR_HA],
                            ["RL_HA_5V", 0, relay_RL_HA],
                            ["FR_HEIGHT_5V", 0, relay_FR_HEIGHT],
                            ["FL_HEIGHT_5V", 0, relay_FL_HEIGHT],
                            ["RR_HEIGHT_5V", 0, relay_RR_HEIGHT],
                            ["RL_HEIGHT_5V", 0, relay_RL_HEIGHT],
                            ["AIR_PRESS_5V", 0, relay_AIR_PRESS],
                            ]

        print(len(sensor_5VON_volt))

    except:
        brd1.close()
        brd2.close()
        brd3.close()
        brd4.close()


