import subprocess
import time
import os

server_name = 'hmcl'
server_ip = '223.171.137.67'
server_passward = 'hmc2020'
current_focus_row = -1
current_focus_col = -1
max_row = 4
max_col = 4
sleep_time =0.1

def find_terminator_shortcut():
    global cmd_split_vert,cmd_split_horiz,cmd_go_left,cmd_go_right, cmd_go_down,cmd_go_up
    home_dir = os.path.expanduser("~")
    file_path = home_dir + '/.config/terminator/config'
    cmd_split_vert = 'Control_R+Shift_R+e'
    cmd_split_horiz = 'Control_R+Shift_R+o'
    cmd_go_right = 'Alt+Right'
    cmd_go_left = 'Alt+Left'
    cmd_go_up  = 'Alt+Up'
    cmd_go_down = 'Alt+Down'

    patterns = {
    "<Shift>": "Shift_R+",
    "<Primary>": "Control_R+",
    "<Super>": "Super+"

    }

    with open(file_path,'r') as f:
        for line in f:
            if 'split_vert' in line:
                split_vert = line.strip()
                for pattern in patterns:
                    split_vert = split_vert.replace(pattern, patterns[pattern])
                cmd_split_vert = split_vert[3+len('split_vert'):]

            if 'split_horiz' in line:
                split_horiz = line.strip()
                for pattern in patterns:
                    split_horiz = split_horiz.replace(pattern, patterns[pattern])
                cmd_split_horiz = split_horiz[3+len('split_horiz'):]

            if 'go_left' in line:
                go_left = line.strip()
                for pattern in patterns:
                    go_left = go_left.replace(pattern, patterns[pattern])
                cmd_go_left = go_left[3+len('go_left'):]

            if 'go_right' in line:
                go_right = line.strip()
                for pattern in patterns:
                    go_right = go_right.replace(pattern, patterns[pattern])
                cmd_go_right = go_right[3+len('go_right'):] 

            if 'go_up' in line:
                go_up = line.strip()
                for pattern in patterns:
                    go_up = go_up.replace(pattern, patterns[pattern])
                cmd_go_up = go_up[3+len('go_up'):] 

            if 'go_down' in line:
                go_down = line.strip() 
                for pattern in patterns:
                    go_down = go_down.replace(pattern, patterns[pattern])
                cmd_go_down = go_down[3+len('go_down'):] 
    
    print("found below shortcut !")
    print("split_vert: ",cmd_split_vert)
    print("split_horiz: ",cmd_split_horiz)
    print("go_left: ",cmd_go_left)
    print("go_right: ",cmd_go_right)
    print("go_down: ",cmd_go_down)
    print("go_up: ",cmd_go_up)

def move_focus(direction):
    global current_focus_row, current_focus_col, max_col, max_row,cmd_go_left,cmd_go_right, cmd_go_down,cmd_go_up
    if direction =="init":
        move_focus("Left")
        move_focus("Up")
        move_focus("Left")
        move_focus("Up")
        move_focus("Left")
        move_focus("Up")
        move_focus("Left")
        move_focus("Up")
        move_focus("Left")
        move_focus("Up")
        move_focus("Left")
        move_focus("Up")
        current_focus_row =1
        current_focus_col =1
        return
    
    if direction =="next":
        if current_focus_col == max_col:
            if current_focus_row == max_row:
                print("next terminal does not exist..!")
            else:
                move_focus("Down")
                move_focus("Left")
                move_focus("Left")
                move_focus("Left")
        else:
            move_focus("Right")
        return
    
    if direction == "Right" or "Left" or "Up" or "Down":
        if direction == "Right":
            cmd = cmd_go_right
        if direction == "Left":
            cmd = cmd_go_left
        if direction == "Up":
            cmd = cmd_go_up
        if direction == "Down":
            cmd = cmd_go_down
        subprocess.run(['xdotool', 'key', cmd])
        time.sleep(sleep_time)
        update_current_focus(direction)
        return
    
def split_h():
    global cmd_split_horiz
    subprocess.run(['xdotool', 'key', cmd_split_horiz])
    time.sleep(sleep_time)

def split_v():
    global cmd_split_vert
    subprocess.run(['xdotool', 'key', cmd_split_vert])
    time.sleep(sleep_time)

def clip(min,max,val):
    if val > max:
        val = max
    if val < min:
        val = min
    return val

def type_cmd(cmd):
    subprocess.run(['xdotool', 'type', cmd])
    time.sleep(sleep_time)
    subprocess.run(['xdotool', 'key', 'Return'])
    time.sleep(sleep_time)

def update_current_focus(direction):
    global current_focus_col, current_focus_row,max_col,max_row
    if direction == "Right":
        current_focus_col += 1
    elif direction == "Left":
        current_focus_col -= 1
    elif direction == "Down":
        current_focus_row += 1
    elif direction == "UP":
        current_focus_row -= 1
    current_focus_col = clip(1,max_col,current_focus_col)
    current_focus_row = clip(1,max_row,current_focus_row)

def split_terminator_init():
    split_v()
    split_v()
    move_focus("Left")
    move_focus("Left")
    split_v()
    move_focus("Left")
    
    split_h()
    split_h()
    move_focus("Up")
    move_focus("Up")
    split_h()
    split_h()
    move_focus("Right")

    split_h()
    split_h()
    move_focus("Up")
    move_focus("Up")
    split_h()
    move_focus("Right")

    split_h()
    split_h()
    move_focus("Up")
    move_focus("Up")
    split_h()
    move_focus("Right")

    split_h()
    split_h()
    move_focus("Up")
    move_focus("Up")
    split_h()
    move_focus("Right")


def enter_ssh():
    global server_name, server_ip, server_passward
    subprocess.run(['xdotool', 'key', 'Alt+a'])
    cmd = 'ssh '+ server_name + '@'+ server_ip
    type_cmd("cd")
    type_cmd(cmd)
    time.sleep(5)
    type_cmd(cmd)
    time.sleep(5)
    type_cmd(server_passward)
    subprocess.run(['xdotool', 'key', 'Alt+o'])
    time.sleep(5)
    
    
def name_terminal(name):
    subprocess.run(['xdotool', 'key', 'Control_R+n'])
    time.sleep(sleep_time)
    type_cmd(name)

def full_screen():
    subprocess.run(['xdotool', 'key', 'Super+Up'])
    time.sleep(1)


def main():
    subprocess.Popen(['terminator']) # Open terminator
    find_terminator_shortcut() # find shortcut from config file
    time.sleep(2) # Wait for the terminals to open
    full_screen()


    split_terminator_init() # predefined 4*4 layout
    move_focus("init") # move focus to left top
    enter_ssh() # all terminal ssh access

    # 11
    name_terminal("roscore")
    type_cmd("roscore")
    move_focus("next")
    time.sleep(5)

    # 12
    name_terminal("MAVROS")
    type_cmd("CHMOD")
    time.sleep(1)
    type_cmd("MAVROS")
    move_focus("next")
    time.sleep(7)

    # 13
    name_terminal("LOCAL")
    type_cmd("LOCAL")
    move_focus("next")
    time.sleep(4)


    # 14
    name_terminal("LASER")
    type_cmd("LASER")
    move_focus("next")
    move_focus("Up")


    # 21-1
    name_terminal("LASER_CUT")
    type_cmd("LASER_CUT")
    move_focus("Down")

    # 21-2
    name_terminal("LASER_CUT_PARAM")
    type_cmd("LASER_CUT_PARAM")
    move_focus("next")


    # 22
    name_terminal("OBSTACLE")
    type_cmd("OBSTACLE")
    move_focus("next")  
    time.sleep(3)
 

    # 23 copy
    name_terminal("FRONT_CAMERA")
    type_cmd("FRONT_CAMERA")
    move_focus("next")   
    time.sleep(5)


    # 24
    name_terminal("DARKNET")
    type_cmd("DARKNET")
    time.sleep(3)
    move_focus("next")   

    # 31
    name_terminal("IMAGE_COMP2")
    type_cmd("IMAGE_COMP2")
    move_focus("next") 

    # 32
    name_terminal("DYN")
    type_cmd("DYN")
    move_focus("next")

    # # 33
    # name_terminal("param load")
    # type_cmd("VERANDA_PARAM")
    # time.sleep(1)

    # 34
    name_terminal("VERANDA")
    type_cmd("VERANDA_MODULE")
    move_focus("next")

    # 41    
    name_terminal("DROP")
    type_cmd("DROP")
    move_focus("next")

    # 42
    name_terminal("LIDAR_THROTTLE")
    type_cmd("LIDAR_THROTTLE")
    move_focus("next")

    # 43
    name_terminal("FDR_NODE")
    type_cmd("FDR_NODE")
    move_focus("next")
    time.sleep(3)

    # 44
    name_terminal("FDR_BAG")
    type_cmd("FDR_BAG")
    move_focus("next")
    
if __name__ == '__main__':
    main()