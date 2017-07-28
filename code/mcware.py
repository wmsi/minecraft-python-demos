#Copyright Crazysqueak
import mcpi.minecraft as minecraft
import mcpi.block as block
import mcpi.minecraftstuff as mcs
import time, random, pickle, datetime
try:
    with open('mcware-lb.5lb','rb') as f:
        leaderboard = pickle.load(f)
except:
    leaderboard = [['Meh',10],['OK',20],['Great',40],['Excellent',80],['CANT TOUCH THIS',100]]
mc = minecraft.Minecraft.create()
mc.setBlocks(-20,20,-20,20,60,20, block.AIR.id)
sb = mcs.ShapeBlock
LOBBYXMIN = -5
LOBBYXMAX = 5
LOBBYZMIN = -5
LOBBYZMAX = 5
LOBBYH = 30+4
class Build:
    def lobby():
        mc.setBlocks(LOBBYXMIN, 30+-1, LOBBYZMIN, LOBBYXMAX, LOBBYH, LOBBYZMAX, 155)
        mc.setBlocks(LOBBYXMIN+1, 30+0, LOBBYZMIN+1, LOBBYXMAX-1, LOBBYH-1, LOBBYZMAX-1, block.AIR.id)
        mc.setBlocks(LOBBYXMIN, 30+-1, LOBBYZMIN, LOBBYXMAX, 30+-1, LOBBYZMAX, block.GLASS.id)
        mc.setBlocks(LOBBYXMIN, LOBBYH, LOBBYZMIN, LOBBYXMAX, LOBBYH, LOBBYZMAX, block.GLASS.id)
        mc.setBlock(0,30+-1,0,block.WOOL.id, 5)
        for pos in [(LOBBYXMIN+1, LOBBYZMIN+1), (LOBBYXMIN+1, LOBBYZMAX-1), (LOBBYXMAX-1, LOBBYZMAX-1), (LOBBYXMAX-1, LOBBYZMIN+1)]:
            mc.setBlocks(pos[0], 30+0, pos[1], pos[0], LOBBYH-1, pos[1], block.LEAVES.id)
        mc.setBlocks(LOBBYXMIN+2, (30+1), LOBBYZMIN, LOBBYXMAX-2, LOBBYH-2, LOBBYZMIN, block.GLASS_PANE.id)
        mc.setBlocks(LOBBYXMIN+2, (30+1), LOBBYZMAX, LOBBYXMAX-2, LOBBYH-2, LOBBYZMAX, block.GLASS_PANE.id)
        mc.setBlocks(LOBBYXMIN, (30+1), LOBBYZMIN+2, LOBBYXMIN, LOBBYH-2, LOBBYZMAX-2, block.GLASS_PANE.id)
        mc.setBlocks(LOBBYXMAX, (30+1), LOBBYZMIN+2, LOBBYXMAX, LOBBYH-2, LOBBYZMAX-2, block.GLASS_PANE.id)
class Clear:
    def lobby():
        mc.setBlocks(LOBBYXMIN, 30+-1, LOBBYZMIN, LOBBYXMAX, LOBBYH, LOBBYZMAX, block.AIR.id)
class Flowers:
    timelimit = 10
    startPos = minecraft.Vec3(0,30,0)
    timeUpKill = True
    instruction = 'Pick all the flowers in 10 seconds'
    cmsg = 'Minigame complete!'
    fmsg = 'Failed to pick the flowers'
    fl = []
    def pre_build():
        mc.setBlocks(-5, 29, -5, 5, 29, 5, block.GRASS.id)
    def build():
        for i in range(5):
            x = random.randint(-5, 5)
            z = random.randint(-5, 5)
            mc.setBlock(x, 30, z, block.FLOWER_CYAN.id)
            Flowers.fl.append(minecraft.Vec3(x, 30, z))
    def loop():
        flowers = 0
        for p in Flowers.fl:
            if mc.getBlock(p.x, p.y, p.z) == block.FLOWER_CYAN.id:
                flowers += 1
        return flowers
    def clear():
        mc.setBlocks(-5, 29, -5, 5, 30, 5, block.AIR.id)
        Flowers.fl = []
    def getPoints():
        ret = [(1, 'Completion')]
        tl = int(etime - time.time())
        tl -= 5
        if tl > 0:
            ret.append((tl, 'Speed bonus'))
        return ret
class Parkour:
    timelimit = 15
    startPos = minecraft.Vec3(0,31,0)
    timeUpKill = False
    instruction = 'Land on as many blocks as you can in 15 seconds'
    cmsg = 'Minigame complete!'
    fmsg = 'Landed on a few too few blocks'
    lb = minecraft.Vec3(0,30,0)
    points = 0
    cp = 0
    cm = 0
    nrt = 0
    def pre_build():
        mc.setBlock(0,30,0, block.OBSIDIAN.id)
    def build():
        Parkour.points = 0
        Parkour.cp, Parkour.cm = 0, 0
        Parkour.nrt = time.time() + 1
    def clear():
        mc.setBlocks(-5, 30, -5, 5, 60, 5, block.AIR.id)
    def loop():
        if Parkour.points < 5:
            Parkour.timeUpKill = True
        else:
            Parkour.timeUpKill = False
        pos = mc.player.getTilePos()
        if mc.getBlock(pos.x, pos.y-1, pos.z) == block.OBSIDIAN.id:
            Parkour.cp += 3
            mc.setBlock(pos.x, pos.y-1, pos.z, block.GLOWING_OBSIDIAN.id)
            Parkour.points += 1
            Parkour.lb = pos.clone()
            x, y, z = 0, 0, 0
            while y == 0 or (x in range(pos.x-1,pos.x+2) and z in range(pos.z-1, pos.z+2)) or (y == pos.y-1):
                x, y, z = -100, -100, -100
                while not x in range(-5, 6):
                    x = random.randint(pos.x-2, pos.x+2)
                while not z in range(-5, 6):
                    z = random.randint(pos.z-2, pos.z+2)
                while not y in range(30, 60):
                    y = random.randint(pos.y-5, pos.y)
            mc.setBlock(x, y, z, block.OBSIDIAN.id)
            mc.setBlocks(x, y+1, z, x, y+2, z, block.AIR.id)
            Parkour.nrt = time.time() + 3
        elif pos.y < 30:
            mc.player.setTilePos(Parkour.lb.x, Parkour.lb.y, Parkour.lb.z)
            Parkour.nrt = time.time() + 3
            Parkour.cm = 1
            Parkour.cp = 0
    def getPoints():
        ret = [(1, 'completion')]
        pp = 1
        ps = Parkour.points
        if ps > 0:
            ps -= 5
        if ps >= 1:
            ret.append((int(ps), 'Block bonus'))
            pp += int(ps)
        return ret
class Treasure:
    timelimit = 30
    startPos = minecraft.Vec3(0, 30, 0)
    timeUpKill = False
    instruction = 'Find as much treasure as you can in 30 seconds (RightClick blocks with a sword to search)'
    cmsg = 'Minigame complete!'
    fmsg = 'You failed to find any treasure'
    treasureloc = minecraft.Vec3(0,0,0)
    points = 0
    def pre_build():
        mc.setBlocks(-5, 29, -5, 5, 29, 5, block.GRASS.id)
    def build():
        Treasure.makeTreasure()
        Treasure.points = 0
    def clear():
        mc.setBlocks(-10, 29, -10, 10, 29, 10, block.AIR.id)
    def getPoints():
        ret = [(1, 'completion')]
        if Treasure.points > 1:
            ret.append(((Treasure.points-1), 'Treasure bonus'))
        return ret
    def makeTreasure():
        Treasure.treasureloc = minecraft.Vec3(random.randint(-5,5), 29, random.randint(-5, 5))
        if score > 30:
            for i in range(3):
                mc.setBlock(random.randint(Treasure.treasureloc.x-3, Treasure.treasureloc.x+3), 29, random.randint(Treasure.treasureloc.z-3, Treasure.treasureloc.z+3), random.randint(3,4))
        else:
            for i in range(3):
                mc.setBlock(random.randint(Treasure.treasureloc.x-3, Treasure.treasureloc.x+3), 29, random.randint(Treasure.treasureloc.z-3, Treasure.treasureloc.z+3), random.choice([block.FARMLAND.id,4]))
    def loop():
        global etime
        if Treasure.points < 1:
            Treasure.timeUpKill = True
        else:
            Treasure.timeUpKill = False
        for hit in mc.events.pollBlockHits():
            if hit.pos.x == Treasure.treasureloc.x and hit.pos.z == Treasure.treasureloc.z:
                Treasure.points += 1
                mc.postToChat('Found treasure! Maybe there\'s even more...')
                etime += 3
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.GOLD_BLOCK.id)
                time.sleep(3)
                mc.setBlocks(-10, 29, -10, 10, 29, 10, block.AIR.id)
                mc.setBlocks(-5, 29, -5, 5, 29, 5, block.GRASS.id)
                pos = mc.player.getTilePos()
                mc.player.setTilePos(pos.x, 30, pos.z)
                Treasure.makeTreasure()
            else:
                mc.setBlock(hit.pos.x, hit.pos.y, hit.pos.z, block.DIRT.id)
class Survive:
    timelimit = 30
    startPos = minecraft.Vec3(0, 30, 0)
    timeUpKill = False
    instruction = 'Don\'t fall down for 30 seconds'
    cmsg = 'Minigame complete!'
    fmsg = '<player> was magnetized to holes'
    def pre_build():
        mc.setBlocks(-5, 29, -5, 5, 29, 5, block.OBSIDIAN.id)
        mc.setBlocks(-5, 32, -5, 5, 32, 5, block.BEDROCK_INVISIBLE.id)
        Survive.timeUpKill = False
    def build():
        Survive.breakblocks = []
        Survive.fixblocks = []
        Survive.nbtime = time.time() + 3
        Survive.nrtime = time.time() + 5
        if 9-int(score/10) > 2:
            Survive.lives = 9-int(score/10)
        else:
            Survive.lives = 2
    def clear():
        mc.setBlocks(-6, 29, -6, 6, 32, 6, block.AIR.id)
    def getPoints():
        ret = [(1, 'completion')]
        Survive.lives -= 1
        Survive.lives /= 2
        if Survive.lives >= 1:
            ret.append((int(Survive.lives), 'lives bonus'))
        return ret
    def loop():
        global etime
        pos = mc.player.getTilePos()
        if mc.getBlock(pos.x, 29, pos.z) == block.OBSIDIAN.id:
            mc.setBlock(pos.x, 29, pos.z, block.GLOWING_OBSIDIAN.id)
            Survive.breakblocks.append((pos.x, 29, pos.z))
        if time.time() > Survive.nrtime:
            for i in range(random.randint(3,int(score/5)+3)):
                x, z = random.randint(-5,5), random.randint(-5,5)
                mc.setBlock(x, 29, z, block.GLOWING_OBSIDIAN.id)
                Survive.breakblocks.append((x, 29, z))
                Survive.nrtime = time.time() + 1
        if pos.x > 5 or pos.x < -5 or pos.z > 5 or pos.z < -5:
            Survive.lives -= 1
            if Survive.lives < 1:
                Survive.timeUpKill = True
                etime = 0
            else:
                mc.postToChat('Lives left: ' + str(Survive.lives))
                mc.setBlock(0, 29, 0, block.OBSIDIAN.id)
                mc.player.setTilePos(0, 30, 0)
                Survive.nbtime += 0.5
        if pos.y < 29:
            Survive.lives -= 1
            if Survive.lives < 1:
                Survive.timeUpKill = True
                etime = 0
            else:
                mc.postToChat('Lives left: ' + str(Survive.lives))
                mc.setBlock(pos.x, 29, pos.z, block.OBSIDIAN.id)
                mc.player.setTilePos(pos.x, 30, pos.z)
                Survive.nbtime += 0.5
        if time.time() > Survive.nbtime and pos.x > -6 and pos.x < 6 and pos.z > -6 and pos.z < 6:
            for blkpos in Survive.fixblocks:
                mc.setBlock(blkpos[0], blkpos[1], blkpos[2], block.OBSIDIAN.id)
                Survive.fixblocks.remove(blkpos)
            for blkpos in Survive.breakblocks:
                mc.setBlock(blkpos[0], blkpos[1], blkpos[2], block.AIR.id)
                Survive.breakblocks.remove(blkpos)
                Survive.fixblocks.append(blkpos)
            Survive.nbtime = time.time() + 0.5
class Path:
    timelimit = 15
    startPos = minecraft.Vec3(0,31,0)
    timeUpKill = False
    instruction = 'Move from the gold block to the diamond block without falling down as many times as possible in 15 seconds'
    cmsg = 'Bonus finished'
    paths = []
    pathid = 0
    points = 0
    bp = 0
    complete = True
    def pre_build():
        mc.setBlock(0, 30, 0, block.OBSIDIAN.id)
    def build():
        Path.points = 0
        Path.bp = 0
        mc.setBlocks(-5, 33, -5, 5, 33, 5, block.BEDROCK_INVISIBLE.id)
        Path.paths.append(mcs.MinecraftShape(mc, minecraft.Vec3(0,30,0), [sb(0,0,0,block.GOLD_BLOCK.id),sb(1,0,0,block.OBSIDIAN.id),sb(2,0,0,block.OBSIDIAN.id),sb(3,0,0,block.OBSIDIAN.id),sb(4,0,0,block.DIAMOND_BLOCK.id)], False))
        Path.paths.append(mcs.MinecraftShape(mc, minecraft.Vec3(0,30,0), [sb(0,0,0,block.GOLD_BLOCK.id),sb(1,0,0,block.OBSIDIAN.id),sb(2,0,0,block.OBSIDIAN.id),sb(3,0,0,block.OBSIDIAN.id),sb(4,0,0,block.OBSIDIAN.id),sb(4,0,1,block.OBSIDIAN.id),sb(4,0,2,block.OBSIDIAN.id),sb(4,0,3,block.OBSIDIAN.id),sb(4,0,4,block.DIAMOND_BLOCK.id)], False))
        Path.paths.append(mcs.MinecraftShape(mc, minecraft.Vec3(0,30,0), [sb(0,0,0,block.GOLD_BLOCK.id),sb(1,0,0,block.OBSIDIAN.id),sb(2,0,0,block.OBSIDIAN.id),sb(3,0,0,block.OBSIDIAN.id),sb(4,0,0,block.OBSIDIAN.id),sb(4,0,1,block.OBSIDIAN.id),sb(4,0,2,block.OBSIDIAN.id),sb(3,0,2,block.OBSIDIAN.id),sb(2,0,2,block.OBSIDIAN.id),sb(1,0,2,block.OBSIDIAN.id),sb(0,0,2,block.DIAMOND_BLOCK.id)], False))
        sbsp = [sb(0,0,0,block.GOLD_BLOCK.id), sb(0,0,-5, block.DIAMOND_BLOCK.id)]
        dirx = 0
        dirz = 0
        currx = 0
        for i in range(1,5):
            currx += 1
            sbsp.append(sb(currx, 0, 0, block.OBSIDIAN.id))
            sbsp.append(sb(currx, 0, -5, block.OBSIDIAN.id))
        currz = 0
        for i in range(50):
            dirx = random.randint(-1, 1)
            dirz = random.randint(-1, 1)
            currx += dirx
            currz += dirz
            sbsp.append(sb(currx, 0, currz, block.OBSIDIAN.id))
        while currz > -5:
            dirx = 0
            dirz = -1
            currx += dirx
            currz += dirz
            sbsp.append(sb(currx, 0, currz, block.OBSIDIAN.id))
        while currz < -5:
            dirx = 0
            dirz = 1
            currx += dirx
            currz += dirz
            sbsp.append(sb(currx, 0, currz, block.OBSIDIAN.id))
        while currx > 0:
            dirx = -1
            dirz = 0
            currx += dirx
            currz += dirz
            sbsp.append(sb(currx, 0, currz, block.OBSIDIAN.id))
        while currx < 0:
            dirx = 1
            dirz = 0
            currx += dirx
            currz += dirz
            sbsp.append(sb(currx, 0, currz, block.OBSIDIAN.id))
        if sb(0,0,-5,block.OBSIDIAN.id) in sbsp:
            sbsp.remove(sb(0,0,-5,block.OBSIDIAN.id))
        Path.paths.append(mcs.MinecraftShape(mc, minecraft.Vec3(0,30,0), sbsp, False))
        Path.pathid = random.randint(0, len(Path.paths)-1)
        Path.complete = True
        Path.paths[Path.pathid].draw()
    def loop():
        global etime
        pos = mc.player.getTilePos()
        if pos.y < 10:
            etime = 0
            Path.complete = False
        if mc.getBlock(pos.x, pos.y-1, pos.z) == block.DIAMOND_BLOCK.id:
            Path.points += 1
            Path.bp += Path.points
            Path.paths[Path.pathid].clear()
            Path.pathid = random.randint(0, len(Path.paths)-1)
            Path.paths[Path.pathid].draw()
            mc.player.setTilePos(Path.startPos.x, Path.startPos.y, Path.startPos.z)
    def getPoints():
        if Path.complete:
            ret = [(1, 'completion')]
        else:
            ret = []
        if Path.points > 0:
            ret.append((Path.points, 'paths cleared'))
            ret.append((Path.bp, 'bonus points'))
        return ret
    def clear():
        mc.setBlocks(-5, 33, -5, 5, 33, 5, block.AIR.id)
        Path.paths[Path.pathid].clear()
class Miner:
    timelimit = 15
    startPos = minecraft.Vec3(0,30,0)
    timeUpKill = False
    instruction = 'Find and mine as many diamonds as possible in 15 seconds'
    cmsg = 'Minigame complete!'
    fmsg = 'No diamonds, no chance!'
    def pre_build():
        mc.setBlocks(-5, 28, -5, 5, 29, 5, block.STONE.id)
    def build():
        Miner.pts = 0
        Miner.ndt = time.time()
        Miner.makeStuff()
    def makeStuff():
        x = random.randint(-5,5)
        z = random.randint(-5,5)
        Miner.diamondpos = minecraft.Vec3(x, 28, z)
        mc.setBlock(x,28,z,block.DIAMOND_ORE.id)
    def loop():
        if Miner.pts == 0:
            Miner.timeUpKill = True
        else:
            Miner.timeUpKill = False
        pos = mc.player.getTilePos()
        if pos.x in range(Miner.diamondpos.x-1,Miner.diamondpos.x+2):
            if pos.z in range(Miner.diamondpos.z-1,Miner.diamondpos.z+2):
                if time.time() > Miner.ndt:
                    Miner.ndt = time.time() + 1
                    mc.postToChat('DIAMONDS DETECTED')
        if mc.getBlock(Miner.diamondpos.x,Miner.diamondpos.y,Miner.diamondpos.z) == block.AIR.id:
            mc.postToChat('There must be more diamonds than that...')
            mc.setBlocks(-5, 28, -5, 5, 29, 5, block.STONE.id)
            mc.player.setTilePos(pos.x, 30, pos.z)
            Miner.makeStuff()
            Miner.pts += 1
    def clear():
        mc.setBlocks(-5, 28, -5, 5, 29, 5, block.AIR.id)
    def getPoints():
        ret = [(1,'completion')]
        if Miner.pts > 1:
            ret.append((Miner.pts-1,'diamonds bonus'))
        return ret
#print('Building lobby')
Build.lobby()
mc.player.setTilePos(LOBBYXMIN+1, 0, 0)
#print('Finalising')
mc.postToChat('Welcome to mcpiware!')
nht = time.time()
dgames = [Survive, Miner, Parkour, Treasure, Flowers]
wt = 0
lwt = 1
lmg = Flowers
#print('Mainloop.\n\n\n\n')
try:
    while True:
        wt += 1
        ppos = mc.player.getTilePos()
        ppo = mc.player.getPos()
        if time.time() > nht:
            mc.postToChat('Stand on the green block and press LSHIFT to start')
            nht = time.time() + 7
            print('Open minecraft to play')
        if ppos.x > LOBBYXMAX or ppos.x < LOBBYXMIN or ppos.z > LOBBYZMAX or ppos.z < LOBBYZMIN or ppos.y > LOBBYH or ppos.y < (30+-1):
            x = ppos.x
            y = ppos.y
            z = ppos.z
            while x > (LOBBYXMAX-1):
                x -= 1
            while x < (LOBBYXMIN+1):
                x += 1
            while z > (LOBBYZMAX-1):
                z -= 1
            while z < (LOBBYZMIN+1):
                z += 1
            while y > (30+0):
                y -= 1
            while y < (30+0):
                y += 1
            Build.lobby()
            mc.player.setTilePos(x, y, z)
        elif ppos.x == 0 and ppo.y == 29.8 and ppos.z == 0:
            #print('\n\n\n\n=====[New Game]=====')
            #print('Preparing game')
            lmgs = [Treasure,Survive,Miner]
            now = datetime.datetime.now()
            baseed = int(((now.day + now.month + now.year) * (now.minute + now.second + now.hour)) / now.isoweekday())
            baseed *= wt
            if baseed > lwt:
                baseed = int(baseed/lwt)
            else:
                baseed = int(lwt/baseed)
            if wt < lwt:
                baseed *= random.randint(wt, lwt)
            else:
                baseed *= random.randint(lwt, wt)
            seed = baseed
            random.seed(seed)
            lwt = wt
            wt = 0
            #print('Running game with seed', seed)
            gameon = True
            mg = False
            mgs = 0
            ns = seed
            score = 0
            target = 20
            Clear.lobby()
            mc.setBlocks(-1, 29, -1, 1, 32, 1, block.AIR.id)
            while gameon:
                mgs += 1
                random.seed(0)
                #print('Starting mg #' + str(mgs) + ' with score ' + str(score))
                #random.shuffle(dgames)
                games = dgames.copy()
                for lmg in lmgs:
                    games.remove(lmg)
                mg = random.choice(games)
                lmgs.append(mg)
                lmgs.pop(0)
                if score >= target:
                    mc.postToChat('BONUS!')
                    #print('This round is bonus round!')
                    mg = Path
                    target *= 3
                random.seed(seed+ns)
                ns = random.randint(seed, seed*3)
                mg.pre_build()
                ret = None
                '''mc.setBlocks(-1, 49, -1, 1, 52, 1, block.BEDROCK_INVISIBLE.id)
                mc.setBlocks(0,50,0,0,51,0,block.AIR.id)
                mc.player.setTilePos(0,50,0)
                time.sleep(0.5)
                mc.setBlocks(-1, 49, -1, 1, 52, 1, block.AIR.id)'''
                mc.player.setTilePos(mg.startPos.x, mg.startPos.y, mg.startPos.z)
                nctime = time.time()
                mc.postToChat(mg.instruction)
                time.sleep(2)
                mc.postToChat('Starting in...')
                for c in range(3, 0, -1):
                    mc.postToChat(str(c))
                    time.sleep(1)
                mc.postToChat('Go!')
                mc.player.setTilePos(mg.startPos.x, mg.startPos.y, mg.startPos.z)
                mg.build()
                etime = time.time() + mg.timelimit
                while time.time() < etime:
                    if time.time() > nctime and (int(etime - time.time())%5 == 0 or int(etime - time.time()) < 5):
                        mc.postToChat(str(int(etime - time.time())))
                        nctime = time.time() + 1
                    ret = mg.loop()
                    if mg.timeUpKill and ret == 0:
                        break
                if mg.timeUpKill and time.time() >= etime:
                    #print('Game over')
                    gameon = False
                    mg.clear()
                    mc.postToChat(mg.fmsg)
                else:
                    mc.postToChat(mg.cmsg)
                    ps = mg.getPoints()
                    for p in ps:
                        mc.postToChat('+' + str(p[0]) + ' ' + p[1])
                        score += p[0]
                        time.sleep(1)
                    mc.postToChat('Your score is ' + str(score))
                    time.sleep(5)
                    mg.clear()
            mc.setBlocks(-1, 29, -1, 1, 32, 1, block.BEDROCK_INVISIBLE.id)
            mc.setBlocks(0,30,0,0,31,0,block.AIR.id)
            mc.player.setTilePos(0,30,0)
            mc.postToChat('Game over')
            mc.postToChat('You scored ' + str(score) + '!')
            time.sleep(5)
            leaderboard.append(['TEMP', score])
            leaderboard = sorted(leaderboard, key=lambda score: score[1])
            nl = []
            for s in reversed(leaderboard):
                nl.append(s)
            leaderboard = nl
            leaderboard.pop()
            idx = -1
            for i in leaderboard:
                idx += 1
                if i[1] == score:
                    break
                else:
                    if idx == len(leaderboard)-1:
                        idx += 1
                    continue
            if idx < len(leaderboard):
                mc.postToChat('You made the leaderboard!')
                mc.postToChat('Please enter your name in the python shell')
                #print('\n\n\n\n')
                #print('Game Over.')
                leaderboard[idx][0] = input('Name: ')
                print('Return to minecraft now.')
            else:
                mc.postToChat('Better luck next time')
                idx = -1
            for lidx in range(len(leaderboard)):
                if lidx == idx:
                    mc.postToChat('#' + str(lidx+1) + '    ' + 'YOU' + '    ' + str(leaderboard[lidx][1]) + '  <<<')
                else:
                    mc.postToChat('#' + str(lidx+1) + '    ' + leaderboard[lidx][0] + '    ' + str(leaderboard[lidx][1]))
            #print('Clearing up')
            mc.setBlocks(-1, 29, -1, 1, 32, 1, block.AIR.id)
            #print('Building lobby')
            Build.lobby()
            mc.player.setTilePos(LOBBYXMIN+1, 0, 0)
            #print('Finalising')
            nht = time.time() + 5
            #print('Done.')
            #print('=====[End game]=====\n\n\n\n')
finally:
    #print('Clearing up')
    mc.setBlocks(-20,20,-20,20,60,20, block.AIR.id)
    #print('Saving leaderboard')
    with open('mcware-lb.5lb', 'wb') as f:
        pickle.dump(leaderboard, f)
    #print('=====[End program]=====\n\n\n\n')
