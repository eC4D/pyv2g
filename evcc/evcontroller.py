from enum import Enum
import random
class EVSimController():
    """Controller Simulator. Either creates a controller for DC or AC case
    """
    def __init__(self, chargingmode):
        #In case of DC
        #Parameters
        self.ac_charging_finish=None
        
        if chargingmode == "DC":
            
            self.maximum_current_limit = 125 #A
            self.maximum_voltage_limit = 400 #
            self.ev_energy_request = 10000 #Wh
            self.ev_target_voltage=400
            self.ev_target_current = 125
            self.ev_maximum_power_limit=50
            #DC EV Status
            self.ev_ready = True
            self.ev_error_code = "NO_ERROR"
            self.evressoc = 83
            self.chargingmode = "DC"
            

        elif chargingmode == "AC":
            self.eamount = 18 #kwh
            self.ev_max_voltage = 230 #V
            self.ev_max_current = 32 #A
            self.ev_min_current = 0 #A
            self.chargingmode = "AC"
        
        self.evstate = EVState.B
        print(f"EV STARTING STATE: {self.evstate}")

    def set_state(self, new_state):
        self.evstate = new_state
        print(f"EV NEW STATE: {self.evstate}")
    
    def get_ev_status(self):
        '''This Method will generate EVStatus elements'''
        ev_status = {
            "EVReady" : True,
            "EVErrorCode" : "NO_ERROR",
            "EVRESSOC" : self.evressoc
        }
        return ev_status

    def charge_up(self):
        """Function that demonstrates the battery charge. At each
        CurrentDemmandRes message SOC will be increased by 10. Can't exceed
        100
        """
        self.evressoc = min(self.evressoc+10,100)
    
    def is_DC_mode(self):
        return self.chargingmode == "DC"

    def is_AC_mode(self):
        return self.chargingmode == "AC"
    

    def AC_charge_complete(self):
        self.ac_charging_finish = random.choice([True, False])
        return self.ac_charging_finish
 
    

class EVState(Enum):
    """Enumaration class describing the EV state. Integer Values represent the
    electrical resistance within the cable in V
    """
    # Not Connected to Charging
    A = 12
    # EV Connected but not yet ready for charging
    B = 9
    # EV connected to CP and ready for charging (No ventilation)
    C = 6
    # EV connected to CP and ready for charging (Ventilation)
    D = 3
    # Problem with Grid no grid connection
    E = 0
    # CP not available
    F = -12
