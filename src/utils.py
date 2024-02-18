from collections import namedtuple

def color_distance(color_1, color_2) -> float: 
    red_ajust = 0.299
    green_ajust = 0.587
    blue_ajust = 0.114
    
    red_difference = (color_1[0] - color_2[0])**2
    green_difference = (color_1[1] - color_2[1])**2
    blue_difference = (color_1[2] - color_2[2])**2

    return (red_ajust*red_difference + green_ajust*green_difference + blue_ajust*blue_difference)**0.5

lua_base_code = """
-- effects
locate_effect = 1322
success_sound = 10963
warning_sound = 10956
error_sound = 10960

construction =  {
    x = nil,
    y = nil,
    z = nil,
    finished = false,
    x_face = 1,
    y_face = 3,
    z_face = 2,
    block_info_index = 4,
    block_id_index = 1,
    color_data_index = 2,
}
_,host_uin = Player:getHostUin()

Chat:sendSystemMsg("#W===============================", host_uin)
Chat:sendSystemMsg("#WScript generator by", host_uin)
Chat:sendSystemMsg("#BMini World Auto Builder", host_uin)
Chat:sendSystemMsg("#Wby #RNuno Lima/PlayCraft", host_uin)
Chat:sendSystemMsg("#W===============================", host_uin)

function set_position(x, y, z)
    if construction.x and construction.y and construction.z then
        Player:playMusic(host_uin,warning_sound,100,1,false)
        Chat:sendSystemMsg("#Y⊘ #WPosition has already been chosen", host_uin)
        return
    end
    construction.x = x
    construction.y = y + 1
    construction.z = z
    World:playParticalEffect(x,y,z,locate_effect,1)
    Player:playMusic(host_uin,success_sound,100,1,false)
    Chat:sendSystemMsg("#G⊙ #WPosition set ".." #Rx:#b"..construction.x.."#n #By: #b"..construction.y.."#n #Gz: #b"..construction.z, host_uin)
end

function build()
    if not(construction.x and construction.y and construction.z) then
        Chat:sendChat("#R⊗  #WUndefined position", 0)
        Player:playMusic(host_uin,error_sound,100,1,false)
        return
    end
    if construction.finished then 
        Chat:sendSystemMsg("#R⊗ #WContruction already done!", host_uin)
        Player:playMusic(host_uin,error_sound,100,1,false)
        return
    end
    for i = 1, #blocks_positions do
        --threadpool:wait(0.0000000000001)
        local x_pos = construction.x + blocks_positions[i][construction.x_face]
        local y_pos = construction.y + blocks_positions[i][construction.y_face]
        local z_pos = construction.z + blocks_positions[i][construction.z_face]
        local block_id =  blocks_pallete[blocks_positions[i][construction.block_info_index]][construction.block_id_index]
        local color_data = blocks_pallete[blocks_positions[i][construction.block_info_index] ][construction.color_data_index]        
        Block:setBlockAll(x_pos, y_pos, z_pos, block_id, color_data)
    end

    construction.finished = true
    World:stopEffectOnPosition(construction.x,construction.y - 1,construction.z,locate_effect)
    Player:playMusic(host_uin,success_sound,100,1,false)
    Chat:sendSystemMsg("#G⊙ #WConstrution completed!", host_uin)
end

function clean()
   if not construction.finished then return end
   for i = 1, #blocks_positions do
        --threadpool:wait(0.0000000000001)
        local x_pos = construction.x + blocks_positions[i][construction.x_face]
        local y_pos = construction.y + blocks_positions[i][construction.y_face]
        local z_pos = construction.z + blocks_positions[i][construction.z_face]
        Block:destroyBlock(x_pos,y_pos,z_pos,false)
   end
    construction.finished =  false
    Player:playMusic(host_uin,success_sound,100,1,false)
    Chat:sendSystemMsg("#G⊙ #WConstruction has been eliminated!", host_uin)
end

function reset()
    if construction.finished then
        Player:playMusic(host_uin,error_sound,100,1,false)
        Chat:sendSystemMsg("#R⊗ #WContruction already done!", host_uin)
        return 
    end
    World:stopEffectOnPosition(construction.x,construction.y - 1,construction.z,locate_effect)
    construction.x = nil
    construction.y = nil
    construction.z = nil
    Chat:sendSystemMsg("#G⊙ #WPosition has been reset!", host_uin)
    Player:playMusic(host_uin,success_sound,100,1,false)
end


function help()
    Chat:sendSystemMsg("/build #WTo build automatically", host_uin)
    Chat:sendSystemMsg("/clean #WTo clean the building", host_uin)
    Chat:sendSystemMsg("/reset #WTo reset build position", host_uin)
    Chat:sendSystemMsg("[Info] #WConstruction is always fair to the north", host_uin)
end

function run_command(input_text)
    commands = {
        build = build,
        clean = clean,
        reset = reset,
        help = help
    }
    local comand = {
            prefix = input_text:sub(0,1),
            option = input_text:sub(2,input_text:len())
    }
    if comand.prefix ~= "/" then
        return
    end
    for key, comand_funtion in pairs(commands) do
        if key == comand.option then
            comand_funtion()
        end
    end
end


function click_event(event)
    if event.eventobjid ~= host_uin then
        return
    end
    set_position(event.x, event.y, event.z)
end 


function chat_input_evenft(event)
    if event.eventobjid ~= host_uin then
        return
    end
    local input_text = event.content
    run_command(input_text)

end
ScriptSupportEvent:registerEvent([=[Player.ClickBlock]=], click_event)
ScriptSupportEvent:registerEvent([=[Player.InputContent]=],  chat_input_evenft)


"""
Block = namedtuple("Block","block_id color_data r g b")
block_color_data =  [
    Block(666, 0, 255, 212, 157),
    Block(667, 0, 255, 255, 255),
    Block(667, 1, 255, 194, 217),
    Block(667, 2, 236, 197, 241),
    Block(667, 3, 219, 203, 243),
    Block(667, 4, 207, 209, 243),
    Block(667, 5, 196, 230, 255),
    Block(667, 6, 188, 237, 255),
    Block(667, 7, 187, 243, 253),
    Block(667, 8, 187, 231, 229),
    Block(667, 9, 210, 238, 210),
    Block(667, 10, 231, 245, 209),
    Block(667, 11, 252, 253, 204),
    Block(667, 12, 255, 255, 205),
    Block(667, 13, 255, 244, 187),
    Block(667, 14, 255, 232, 186),
    Block(667, 15, 255, 211, 196),
    Block(668, 0, 251, 112, 0),
    Block(668, 1, 255, 212, 219),
    Block(668, 2, 251, 160, 161),
    Block(668, 3, 255, 148, 185),
    Block(668, 4, 216, 152, 226),
    Block(668, 5, 188, 163, 229),
    Block(668, 6, 167, 174, 228),
    Block(668, 7, 255, 250, 123),
    Block(668, 8, 135, 220, 255),
    Block(668, 9, 134, 230, 244),
    Block(668, 10, 134, 210, 205),
    Block(668, 11, 173, 222, 174),
    Block(668, 12, 207, 233, 172),
    Block(668, 13, 241, 247, 163),
    Block(668, 14, 255, 254, 164),
    Block(668, 15, 255, 232, 136),
    Block(669, 0, 164, 40, 184),
    Block(669, 1, 255, 177, 151),
    Block(669, 2, 226, 211, 209),
    Block(669, 3, 0, 0, 0),
    Block(669, 4, 240, 119, 120),
    Block(669, 5, 1, 161, 240),
    Block(669, 6, 195, 108, 209),
    Block(669, 7, 156, 121, 214),
    Block(669, 8, 127, 139, 212),
    Block(669, 9, 105, 187, 255),
    Block(669, 10, 83, 202, 255),
    Block(669, 11, 81, 215, 235),
    Block(669, 12, 81, 189, 180),
    Block(669, 13, 135, 206, 138),
    Block(669, 14, 183, 221, 135),
    Block(669, 15, 231, 239, 122),
    Block(670, 0, 151, 209, 255),
    Block(670, 1, 255, 221, 82),
    Block(670, 2, 255, 190, 80),
    Block(670, 3, 255, 143, 105),
    Block(670, 4, 197, 176, 171),
    Block(670, 5, 250, 247, 249),
    Block(670, 6, 251, 86, 84),
    Block(670, 7, 248, 66, 127),
    Block(670, 8, 179, 74, 196),
    Block(670, 9, 132, 90, 203),
    Block(670, 10, 97, 111, 200),
    Block(670, 11, 69, 171, 255),
    Block(670, 12, 43, 189, 255), 
    Block(670, 13, 40, 205, 228), 
    Block(670, 14, 40, 172, 161),
    Block(670, 15, 107, 194, 111),
    Block(671, 0, 255, 223, 67),
    Block(671, 1, 222, 233, 91),
    Block(671, 2, 255, 247, 92),
    Block(671, 3, 255, 209, 42),
    Block(671, 4, 255, 173, 40),
    Block(671, 5, 255, 116, 70),
    Block(671, 6, 169, 141, 133),
    Block(671, 7, 235, 232, 234),
    Block(671, 8, 255, 69, 56),
    Block(671, 9, 244, 31, 103),
    Block(671, 10, 255, 211, 134),
    Block(671, 11, 108, 60, 191),
    Block(671, 12, 66, 84, 189),
    Block(671, 13, 35, 155, 254),
    Block(671, 14, 3, 175, 255),
    Block(671, 15, 0, 195, 221),
    Block(672, 0, 215, 228, 60),
    Block(672, 1, 80, 181, 84),
    Block(672, 2, 146, 202, 77),
    Block(672, 3, 0, 155, 142),
    Block(672, 4, 255, 243, 62),
    Block(672, 5, 255, 200, 7),
    Block(672, 6, 255, 157, 0),
    Block(672, 7, 255, 90, 36),
    Block(672, 8, 148, 114, 103),
    Block(672, 9, 82, 54, 48),
    Block(672, 10, 240, 59, 55),
    Block(672, 11, 227, 28, 100),
    Block(672, 12, 149, 37, 178),
    Block(672, 13, 99, 55,185),
    Block(672, 14, 60, 76, 179),
    Block(672, 15, 255, 113, 0),
    Block(673, 0, 252, 102, 152),
    Block(673, 1, 0, 178, 202),
    Block(673, 2, 0, 142, 128),
    Block(673, 3, 70, 166, 74),
    Block(673, 4, 130, 185, 69),
    Block(673, 5, 201, 209, 53),
    Block(673, 6, 255, 224, 55),
    Block(673, 7, 255, 185, 0),
    Block(673, 8, 255, 145, 0),
    Block(673, 9, 255, 84, 31),
    Block(673, 10, 127, 88, 75),
    Block(673, 11, 166, 164, 165),
    Block(673, 12, 221, 49, 49),
    Block(673, 13, 204, 25, 95),
    Block(673, 14, 129, 32, 169),
    Block(673, 15, 85, 47, 175),
    Block(674, 0, 102, 100, 101),
    Block(674, 1, 26, 122, 219),
    Block(674, 2, 2, 141, 218),
    Block(674, 3, 0, 156, 174),
    Block(674, 4, 0, 125, 112),
    Block(674, 5, 59, 147, 63),
    Block(674, 6, 109, 165, 58),
    Block(674, 7, 184, 186, 45),
    Block(674, 8, 255, 199, 47),
    Block(674, 9, 255, 166, 0),
    Block(674, 10, 255, 128, 0),
    Block(674, 11, 241, 77, 26),
    Block(674, 12, 114, 79, 68),
    Block(674, 13, 123, 121, 122),
    Block(674, 14, 175, 255, 245),
    Block(674, 15, 182, 21, 91),
    Block(675, 0, 198, 196, 197),
    Block(675, 1, 72, 40, 167),
    Block(675, 2, 42, 55, 154),
    Block(675, 3, 22, 105, 200),
    Block(675, 4, 2, 123, 197),
    Block(675, 5, 0, 136, 149),
    Block(675, 6, 0, 109, 96),
    Block(675, 7, 187, 255, 93),
    Block(675, 8, 89, 144, 49),
    Block(675, 9, 166, 163, 38),
    Block(675, 10, 255, 174, 39),
    Block(675, 11, 255, 148, 0),
    Block(675, 12, 228, 252, 255),
    Block(675, 13, 227, 69, 22),
    Block(675, 14, 255, 242, 0),
    Block(675, 15, 50, 65, 166),
    Block(676, 0, 0, 198, 172),
    Block(676, 1, 143, 15, 82),
    Block(676, 2, 78, 21, 146),
    Block(676, 3, 51, 28, 152),
    Block(676, 4, 27, 36, 132),
    Block(676, 5, 14, 74, 168),
    Block(676, 6, 1, 90, 162),
    Block(676, 7, 0, 99, 104),
    Block(676, 8, 0, 80, 67),
    Block(676, 9, 28, 97, 33),
    Block(676, 10, 54, 109, 31),
    Block(676, 11, 136, 123, 24),
    Block(676, 12, 255, 132, 24),
    Block(676, 13, 255, 115, 0),
    Block(676, 14, 241, 84, 0),
    Block(676, 15, 200, 56, 13),
    Block(677, 0, 111, 28, 161),
    Block(677, 1, 69, 68, 69),
    Block(677, 2, 233, 0, 0),
    Block(677, 3, 207, 18, 102),
    Block(677, 4, 178, 0, 255),
    Block(677, 5, 103, 0, 244),
    Block(677, 6, 50, 82, 255),
    Block(677, 7, 43, 102, 255),
    Block(677, 8, 0, 150, 244),
    Block(677, 9, 0, 191, 221),
    Block(677, 10, 192, 29, 29),
    Block(677, 11, 0, 207, 87),
    Block(677, 12, 105, 229, 24),
    Block(677, 13, 183, 242, 0),
    Block(677, 14, 255, 222, 0),
    Block(677, 15, 255, 177, 0),
    Block(678, 0, 31, 141, 239),
    Block(678, 1, 232, 46, 0),
    Block(678, 2, 65, 40, 37),
    Block(678, 3, 0, 0, 0),
    Block(678, 4, 255, 24, 71),
    Block(678, 5, 255, 0, 91),
    Block(678, 6, 223, 0, 255),
    Block(678, 7, 106, 32, 255),
    Block(678, 8, 64, 93, 255),
    Block(678, 9, 43, 125, 255),
    Block(678, 10, 0, 182, 255),
    Block(678, 11, 0, 237, 255),
    Block(678, 12, 30, 241, 190), 
    Block(678, 13, 0, 238, 123),
    Block(678, 14, 124, 255, 3),
    Block(678, 15, 208, 255, 0),
    Block(679, 0, 98, 66, 57),
    Block(679, 1, 255, 203, 0),
    Block(679, 2, 255, 150, 0),
    Block(679, 3, 255, 63, 0),
    Block(679, 4, 248, 248, 252),
    Block(679, 5, 101, 129, 145),
    Block(679, 6, 255, 85, 86),
    Block(679, 7, 255, 66, 135),
    Block(679, 8, 235, 66, 255),
    Block(679, 9, 130, 80, 255),
    Block(679, 10, 87, 113, 255),
    Block(679, 11, 71, 143, 255),
    Block(679, 12, 67, 203, 255),
    Block(679, 13, 25, 255, 255),
    Block(679, 14, 105, 255, 228),
    Block(679, 15, 110, 249, 182),
    Block(680, 0, 48, 129, 52),
    Block(680, 1, 250, 255, 68),
    Block(680, 2, 255, 255, 0),
    Block(680, 3, 164, 211, 105),
    Block(680, 4, 255, 177, 67),
    Block(680, 5, 255, 114, 67),
    Block(680, 6, 217, 224, 230),
    Block(680, 7, 88, 114, 127),
    Block(680, 8, 255, 143, 134),
    Block(680, 9, 255, 133, 179),
    Block(680, 10, 246, 133, 255),
    Block(680, 11, 188, 141, 255),
    Block(680, 12, 147, 164, 255),
    Block(680, 13, 136, 183, 255),
    Block(680, 14, 134, 224, 255),
    Block(680, 15, 139, 255, 255),
    Block(681, 0, 208, 41, 42),
    Block(681, 1, 194, 255, 211),
    Block(681, 2, 214, 255, 150),
    Block(681, 3, 255, 255, 135),
    Block(681, 4, 255, 255, 147),
    Block(681, 5, 255, 237, 133),
    Block(681, 6, 255, 216, 134),
    Block(681, 7, 255, 164, 134),
    Block(681, 8, 151, 170, 182),
    Block(681, 9, 58, 74, 82),
    Block(681, 10, 255, 232, 237),
    Block(681, 11, 255, 224, 237),
    Block(681, 12, 251, 221, 254),
    Block(681, 13, 243, 232, 255),
    Block(681, 14, 234, 234, 255),
    Block(681, 15, 225, 242, 255),
    Block(682, 0, 35, 34, 34),
    Block(682, 1, 219, 254, 255),
    Block(682, 2, 219, 249, 247),
    Block(682, 3, 232, 251, 232),
    Block(682, 4, 249, 255, 233),
    Block(682, 5, 255, 255, 229),
    Block(682, 6, 255, 255, 231),
    Block(682, 7, 255, 253, 222),
    Block(682, 8, 255, 248, 225),
    Block(682, 9, 255, 235, 234),
    Block(682, 10, 126, 149, 163),
    Block(682, 11, 40, 52, 58),
    Block(682, 12, 0, 0, 0),
    Block(682, 13, 0, 0, 0),
    Block(682, 14, 0, 0, 0),
    Block(682, 15, 0, 0, 0)
]