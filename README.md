# bilibili-crawler
This is a crawler to scrape live commenting on bilibili(https://www.bilibili.com/) vidoes.
- take guojierui's video as sample data
- generate word cloud based on key words

## example
Video url: https://www.bilibili.com/video/BV1cC4y1a7xA  
### commands
python3 live_comment_crawler.py  
### live comment results
['帽子不错', '来者何人', '不是时差，是纽约纬度高，在苏格兰甚至晚上十点天都亮着', '这普通话说越说越好了', '哈哈，福建的上空经常有直升机，我见过', '新冠是可以通过眼睛传染的对吧？我记得', '注意安全啊', '战地记者', '注意安全', '？？？？？', '好心疼', '人家郭杰瑞的口罩已经完全拉开了，只是鼻子太高看起来那样而已，有些弹幕真的找打', 'Helicopter', 'Zara 意思不就是砸了', '天啊', '和平美利坚  枪战每一天', 'ducker~', '？？？？？？？', '哈哈', '纽约纬度高...白天很长', '民 风 淳 朴', '？？？？？', '公吧一眼认出佳能戴尔', '千玺的歌！', '押韵好评', '建国，危', '发音好清晰', '我去，口罩呢', '注意安全', '？？？', '这个属实憨批', '川普暴露了', 'Gay protester', '笑了，明摆着一个川粉还明白人？排挤欺压有色人种被她说成“互相歧视”？睁眼说瞎话就是', ' 太过分了这个', '注意安全', 'black lives matter', '为了正义！', '哈哈哈哈哈哈', '？？？？？？', '哈哈哈', '为啥不整个喇叭', '真惨', '甩锅罢了', '大城市啊，玻璃都是实木的', '注意安全', '你把口罩带好了', '美团外卖', '注意安全', '建国同志要小心啊', '？？？？？', '3个月？', '美团小哥', '注意安全', '知道为什么没有保护亚裔的活动吗？因为亚裔还有家，非裔没有', 'suai！', '心疼呀！', '0元抢购', '心疼', '毫不犹豫的答案', '卧槽？', '莫斯科1942.12', '易烊千玺的歌诶……', '63一点都看不出来，好壮实', '太过分了，赤裸裸的歧视', '在家睡觉不香吗', '我现在才认识到祖国56个民族一律平等的原则有多重要', '你63了我怎么看不出来？？？', '社会制度不一样，解决枪的问题就要大革命', '宵禁的原因就在这了', '注意安全', '艾莎！！', '注意安全', 'omg', '注意安全 杰瑞', '......健壮的大爷', '？？？？真难受', 'zara大可不必', '生在中国好幸福', '利益', '少数理智人啊', '不逮捕砸店的人难道还要 发个奖章？？', '建国好样的', '马奇诺防线好吧', '注意安全！！！', '您们需要马列主义', '不露脸是人家的权利，做任何事的前提是保护好自己', '美国州法最大，不能控制', '那就解决教育问题', '保护我方川普', '注意安全', '我也卡。。？', '。。。', '元芳你怎么看', '是你吗甜瓜', 't\u2006t\u2006t', '保护', '佩罗西：美丽的风景线', '危', '印第安人呢？', 'BGM好像弹起我心爱的土琵琶，第一句歌词“西边的太阳快落山了”', '帽子不错', '这个好帅', '卧槽？', '凶好大', '哈哈哈', '6666', '注意安全', '人心中的成见是一座大山 和枪没多大关系', '杜兰特？。？', '保护建国同志', '川普（危）', '？？？？？？', '亚裔更惨', '其实亚裔在美的地位比黑还低', '？？？？？？', '注意安全', '太悲哀了', '我想啸', '注意安全', '准备好了有点好笑', '注意安全', '你是谁？', '说心疼的，去广粥看看？', '这个过分了', '确实', '⭐️⭐️⭐️⭐️⭐️', '对不起这个我笑了', '⭐️⭐️⭐️⭐️⭐️', '前面说中国海纳百川的，你怕不是没看到b站的反黑人士', '犹太资本', '注意安全', '我要去米国卖木板', '这TM算什么？亚裔不乖乖交出钱包就是违法', '你们无聊不无聊？看见个绿色帽子就高潮？', '你知道我们这里有几个月嘛，知足吧', '听你说话我感觉自己是听得懂英语的', '我', '我的心', '麦迪是你', '？？？？？？？？？？？？？？？？？？？？？', '保护', 'scarloxd?', '这太过了?', '啊。。。这。。。', '战地记者', '注意安全', '黑人就是扛老', '耳边响起手风琴声', '自己国家不待着，非要去别的国家', 'James Charles？', '好帅', '有点想哭', '？？？？？？？？？？', '美团外卖', '美团小哥', '注意安全！！', '口罩戴好啊', '这口罩戴的有一手的', '这姐们才是真正的明白人，美国现在就是身份政治', '哈哈哈哈哈', '明白人明白人', '明白人明白人', '明白人明白人', '明白人明白人', '明白人明白人', '明白人明白人', '明白人明白人', 'gta6', 'rap', '好帅啊！', '希望我去美国读硕士的时候，那里会变得很棒', '是保护那些人不被警察正当防卫吧', '注意安全啊', '这么采访不怕被传染吗', '注意安全', '富国银行', '脏辫小哥像小卡', '拖把？', '骑车的都带了头盔', '自由', '？？？？？？？？过分了吧', '这个是个明白人，刚刚那个女的说的我赞同', '注意安全', '注意安全', '亚裔最注重隐私和保护自己', '亚裔最注重隐私和保护自己', '电动车抢镜', '？？？', '好大！！！', '好像疤王，帅哦', '范思辙？？范闲呢？', '帅', '真的有点...', '枪支触犯到了很多人的利益', '那为啥白人不遣返欧洲', '这个不辣', '注意安全！！！', '打我姚明！打我姚明！', '对线军工复合体', 'zara算了，没人会抢你的', '川普住白宫委屈了', '好可怜', '我...有点怕', '口罩要掉了', '注意安全', '战地记者，注意安全', '比中指哈哈哈', '我擦', '真战地记者', '你们需要中国制造的玻璃', '注意安全', '肺炎不管了？', '美国历史一共两百年', '美国的抗议缺少一个像马丁路德金一样的leader，不然会更有意思', '这个还只是和平游街', '那个黑人老哥骑的是小牛n1', '来你妹的中国，来了你养，真是圣母心泛滥', '明白人', '哈哈哈哈哈哈', '心疼', '泪目', '哈哈哈哈川普', '战地记者郭杰瑞', '杰瑞是白人....所以还好...', '当不欺压他人时，只能压榨自已', '天道好轮回', '？？？？？', '欺负老实人', '川普快回来吧', '.啊～！', '自由美利坚', '讲真的，黑人雄起，大乱一番，他就好了，全是惯出来的', '央视来了', '注意安全！！', '？？？？？？？？？？？？？？？？？？？？？', '为啥要打码啊', '场上唯一明白人', '天哪', '天哪', '川普大楼', '但抗议又能改变什么呢 ', '对对对对 小姐姐明白人', '亚裔分明更惨，你们在心疼啥', '这是一道美丽的风景线', '好多自行车', '他们好勇敢啊，，，', '没有歧视，老美怎么卖弹药。', '中文加密', '中文加密？', '达能', '哇，这？？？有点', '保护', '明白人', '注意安全啊', 'h', '易烊千玺的bgm！', 'bgm灾！', '说的对', "ofc it's USA", '唉', '这么搞的吗，，，', '美国外卖', '保护', '注意安全', '战地记者', '注意安全', '-注意安全', '谁是罪魁祸首就去找谁，伤及无辜和强盗有啥区别', '？？？', '163', '大场面啊哈哈哈哈', '“明白人”', '希望能有好转', '注意安全！！！', '？？', '风景', '注意安全', '？', ' 注意安全', '深圳卫视美国战地记者郭锥锥', '保护我方，战地记者，杰瑞郭~~', '锅某注意安全，好担心', '注意安全啊', '战地记者郭杰瑞', '太过分了', '明白人', '明白人', '哈哈哈哈哈哈哈', '？？？？', '你居然敢说黑人， 不说非裔美国人', '注意安全', '淳朴的民风', '2333', '哈哈哈哈', 'amazing', '我的妈', '我天，必须改变了。', '好混乱啊', '每个人都觉得自己正义', '怎么没人心疼印第安人', '美国是个移民城市，他们把本地土著都干掉以后，互相折磨', '前面那个说得对啊。大家互相针对啊。', '政治正确变成暴力和笑话了', '注意安全啊！', '注意安全！', '？？？？？？？？？', '不知道说什么舒服了的什么心态', '注意安全', '注意安全', '注意安全', '？？？？', '涅槃的t恤！', '战地记者', 'no justice，no peace', 'obama？', '来中国那个你养？', '口罩戴的不标准，还在人这么多的重灾区，要注意呀!', '战 地 记 者 郭 杰 瑞', '第一眼看成美团外卖', '卧槽', '不是，是会被当成你把东西塞到口袋里想带走', '注意安全', 'nirvana', '太过分了..', 'up注意安全', '注意安全呐！', '戴口罩哈哈哈哈', '注意安全', '注意安全', '自由的国度', '？', '注意防护病毒啊', '大爷应该是有经历过很多', '准备迎接冲击', '确实', '战地记者', '17【加油加油加加油】', '美丽风景线', '天呐', '哎', '战地记者', '？？？？？？？', '戴口罩！', '天呐!', '？？？？？？？？？？？', '美国好乱', '注意安全', '做戏的很多，实质进展很少', '以后也不会有改变，如果黑人还是这样不自强自律', '所以最奇怪的就是黑人已经这样了，还会把伤口带给亚裔，自己有多无辜呢？', '这就是自由吗 爱了爱了', 'hey,这人的衣服上都是汉字和熊猫耶', '注意安全啊', '3', '川普hhh', '后面的艾莎', '他们带的口罩大部分都没用', '注意安全', '妈呀这种环境我好怕出事', '消逝的光芒诚不欺我', '注意安全杰瑞', '？？？？？？？？？', '帽子不错', '？？', '战地记者', '注意安全', '红脖子', '啊', '注意安全', '注意安全', '注意安全', '我很难不讨厌一个欺压我的人。', '黑人贸易把那些没有文化的人带过来，所以白天肯定歧视，但是在美国的黑人都现在有素质的呀！', '押韵', '注意安全', '美丽的风景线', '注意危险', '哈哈哈哈哈', '哈哈哈哈哈', '天呐', '明白人', '加油', '财你妹财富密玛真无聊', '财你妹财富密玛无聊', '注意安全啊', '直升机，我上次台风就看到过', '川普希望这样，他不好意思说群体免疫', '苏卡不列', '想每人发个大声公', '黑豹', '这是什么痛苦印记', '这只是因为他违反交通规则他自己还不知道吧哈哈哈', '谁看见后面的艾莎了？', '今天晚上我们去把川普的家炸了吧', '乌拉', '有人吗', '晚上八点还这么亮可能是因为纬度吧（纽约纬度和中国东北差不多）', '注意安全', '天呐', '注意安全！', '需要一个马丁路德金', '声音有一点像cj', '国际通用手势', '战地记者郭杰瑞，注意安全', '这个是真实的，黑人晚上出门去个便利店也要整理仪容，就是怕被警察误会', '56个名族的大家庭真好', '他们必须得有组织和纲领', 'ducker', '黑人说英语好爽啊', '还有黑豹', '老郭是犹太人', '居然有的白人还是追求平等', '黑人就是不显老阿', '帽子不错。', 'freedom', '外国人英语好的那个，你母语不好吗？', '为什么不拿喇叭和小蜜蜂啊？光吼好吃力。', '需要客观一点', '哇哈哈川普', '哎哎哎好惨', '哈哈哈', '郭杰瑞注意安全', '电击枪，我知道，奶奶和爷爷家里有...对不起，来错地方了', '注意安全', '哈哈哈哈', '亚裔zui\u2006zh\u2006y', '戴口罩啊', '亚裔真最被歧视', '真的很惨', '为什么不戴口罩 说话不应该带上吗', 'all lives matter', '说的对', '这女生太棒了', '娱乐至上的国家', '黄皮肤依然会被歧视', '注意安全', 'protest', 'PTSD创伤性应激障碍', 'blm！', '注意安全', '美团外卖？', 'helicopter', 'definitely', '？？？？', '注意安全', '注意安全', '然而在美国最受气势的还是华裔', '可怕', '没枪怎么保护家园', '这姐们怕不是王骁粉丝', '篝火晚会?', '保 护 警 察', '气派', '带申公豹', '注意安全', 'USA的真实风景', '看到那女的我笑了', '川普大叔', '奥巴马', '川普过分了', '绿的', '注意安全', '战   地   记   者   郭   杰   瑞', '注意安全', '虽然很毁气氛，但是帽子颜色不错', '口怕', '公路车和固齿好多诶', '注意安全', '心疼啊', '哎', '天啊', '建国同志要保护好自己啊！组织支持你！', '好好玩哦', '美团？', '☆☆★★★', '法国军礼', '注意安全', '战地记者', '？？？？？？？？？？？？？', '自由美利坚枪战每一天', '自由美利坚枪战每一天！', '自由美利坚枪战每一天.', '自由美利坚枪战每一天!!!', '精彩', '大懂朝皇宫', '特朗普第0冲锋队', '明白人出来了', '真GTA', '哇，中文这么好！', '注意安全', '不知道奥巴马会有什么样的表示', 'Nirvana', '华尔街大佬不屑一笑', '注意安全', '还有人在旁边拍照真行', '哎', 'kanyewest', '哇', '注意安全！！', '注意安全！', '帽子挺好的', '注意安全', '唉。。', 'never change 太真实了', '旁边的美国人：？？？加密通话？', '注意安全啊', '哈哈哈哈哈哈哈哈哈哈哈', '好可怜', '说得对', '哇⊙∀⊙！艾莎', '艾莎', '她确实没说错', '美国应该改名丑国', '特朗普是垃圾，滚', '特不靠谱真的不太靠谱', '心疼啥？这个刻板印象还不是黑们自己作的？', '建国同志注意安全', '哈哈哈哈', '保 护', '建国以来甚至独立战争前就有的问题', '有些州就有禁枪', '和平解决事情', '美团外卖盖茨比', '说的对', '美团外卖发声', '抢劫是自由的事，凭什么管我？（狗头）', '篝火晚会！', '美国变得很棒？', '美国黑人只要双手插袋就可能被认为是掏枪', '几百年？  米国有几百年吗', '哈哈哈哈哈哈哈哈哈哈哈', '明白人', '华人在美国更受歧视', ' 这个老哥说的才对', '杰瑞注意安全啊', '木头有好多洞，不会是弹孔吧', '注意安全', '天呐', '保护我方建国同志！', 'all lives matter', '大玻璃好贵的', '注意安全', '好帽子', '口罩漏风了兄dei', '这是个明白人', '夏令时tinhsh', '川普现在，在地下城堡', '把木板烧了不就好了？', '这真的太过分了', '这时候有人开枪', '注意安全', '注意安全', '保护川普的家', '63岁，那他小的时候确实经历过种族隔离', 'elsa', '这明明是iPhone 5', '兄弟我这里有一本毛概#滑稽', '这个是中国人', '人口密集。。。。', '搞事情', '这个人哈哈哈', '战地记者郭杰瑞', '保护我方川建国', '看这个警察的手', '美团外卖？！', '哇帅哥', '好像j cole啊哈哈哈哈', '民风淳朴', '建国同志辛苦了', '说实话，亚裔的待遇不比黑人好', 'of course  耶耶耶耶', '回非洲不就得了大家都妈', '支持川普', '明白人', '混入其中', '混入其中', '信你个鬼', '棒', '美团？', '戏如人生', '戏如人生', '明白人', '明白人', '美团小哥', '注意安全', '太难受了', '爽啊', '零元购笑死', '中美民众的观念有非常大的差距', '俗话说就是闲出屁了，长时间不工作真的会让人心里出问题', 'Door\xa0secured', 'Door\xa0secured', '我爱中国', '战地记者', 'Zara想好多', '注意安全', '保护川建国同志', '这也太可怕了吧', '？？？？？？', '我很难不讨厌一个欺压我的人。', '注意安全', '别说，不难看', '战地记者', '主义注意安全', '好可怕', '不是只有黑人有这个问题，华人同样有这个问题', '63？', 't病毒', '注意安全', '见证历史', '战地记者', '这什么逻辑？', '美团小哥？', 'All lives matter', '听到这我一经掏出了一把机关枪和去纽约的机票', '马塞洛？', '背景音乐！', '我仿佛听到了洛基', 'Doors barricaded! Walls reinforced! ', '哈哈', '排面', '注意安全哦', '注意安全', '注意安全！！！', '注意安全！！', '小心啊', '可怜', '注意安全', '说的对 其实亚裔被歧视的更严重..', '游荡在云端念着你', '注意安全', '好可怕', '太可悲啊', '可以换中国制造的钢化玻璃', '什么，又被针对了？', '天', '造孽', '心疼个毛线', '郭锥把防护镜戴上！那唾沫星子哎呀妈呀', 'hahahahahh 准备好了', '这亚裔八成是个日本人 日本人比较注重隐私', 'OMG', '0元抢购活动啊，现在美国有类似活动', '美团外卖', '但是权利在白人手里', '还好郭锥是白人', '保护好自己', '好好好', '？？？？？？', '全境封锁', '注意安全', '川普？', '瓜哥？', '歧视亚裔更严重', '衣服上真的有汉字唉', '没错', '注意安全', 'Elsa！！！！elsanna冲鸭', '保护川建国同志，他在帮忙美国成长doge', '回非洲吧，安全一点', '印第安人怎么说？都快灭种了', '亚裔受歧视比黑人还惨', '有种族肯定有歧视，说的没错', '天黑黑人就隐身了', '不是国产的', '木头就砸不碎吗？', '注意安全', '注意安全', '老郭，注意安全啊', '保护', '还是中国好', '建国同志这个人生活作风问题大大的', '小心啊', '注意安全', '天呐。。。这也太。。。。', '夜黑风高抢劫夜', '哭了', '战地记者', '保护', '？？？？？？？？？', '建国同志小心', '啊？？？', '注意安全', 'trump口罩瞩目', '注意安全', '！！！！', '未曾设想的道路', '你可以发现不少受访黑人的生活水平和文化水平并不差……', '镰刀和锤子', '但是有一说一，美国人想赶川普下台这件事没毛病', '狗窝笑死我了', '讲出粤语？', '白左误国', '白左误国', '民粹主义可怕', '战地记者，，，，，', 'bbc', '美国可真是太刺激了', '亚裔可能比黑人惨，因为没有抗议过', '这是Logan Paul？', '啊这', '刀锋？是你么？', '难过', '随便说一下，在我国上次抗议是因为美国打我们大使馆', '庆余年也准备好了', '印第安人表示很淦', '互相歧视', '果然是亚裔', '蹦迪', '换成木头方便点燃', '一定要注意安全呀', '战地记者', 'payday2', '泪目', '天啊', '你们需要轩辕黄帝', 'you know', '带好口罩', '战地记者', '天呐', '克莱呢', '注意安全', '美丽的风景', '注意安全', '黄种人在美国地位还不如黑人', '真是闲的', '美团外卖哈哈哈', '要死的亚裔不会这样', '注意安全', '亚裔最底层', '美团小哥又来了', '挡脸可能是因为是留学生什么的', '因为中国禁枪的问题，所以警察执法手段更和平', '人家都是奢侈品店Zara你跟着凑什么热闹', ' 帽子着实不错', '来者何人', '唉', 'G  T  A  6', '郭德纲准备好了吗', '我以为你要拔枪', '注意安全', '哈哈哈哈哈哈哈哈哈哈', '？？心疼', '魔幻世界', '战  地  记  者', '纽   约   故   宫', '几百年？喝多了吗？', '呵呵', '？？？？？？', '注意安全，和平抗议', '？', '过去的领导者在想办法缓和矛盾，川普在激化矛盾', '民风淳朴美利坚', '确实', '饿了么不配拥有姓名', '川普家在纽约呀', '天呐！好可怕！为什么会这样！', '？？？？？？？？', '5星通缉', '不要为你的女权）找借口', '曼达洛人！', '其实美国大部分抗议还是挺文明的', '嗯怎么感觉听上去像是没事干了', '郭锥注意安全', '哈哈哈哈哈', '哈哈哈？', '怎么还有笑的？', '过分了', '注意安全', '郭杰瑞口罩带好啊 鼻子那里要捏紧', '明白人', '？？？？？？？？？', '发型好评', '工 人 纠 察 队', 'ghhhhh', '咯饿肚子 ', '佩服这些白人', '为了正义', '看到美国这样，我为何这么高兴！！！', '美国警察没有黑人吗？', '可以换成中国制造', '易烊千玺的灾！！！！', '哈哈哈哈哈哈哈哈哈哈', '趁火打劫确实不应该', '口罩：trump2020', '啊', '人类的悲哀', '唯有胜者即是正义', '太tm真实了', '在中国口袋随便插', '对比一下这体格吧', '绿色代表和平', '奥观海', '小姐姐当心点，现在美国乱的啊', '最美丽的风景区', 'BLM万岁', '央视驻美利坚战地记者', '蒙斯克皇宫', '为了字由', '字由平等国', '注意安全啊', '保护我方战地记者', '感谢老郭发来报道', '坚果小心', '注意安全', '？？？？？？？？？？？？？？', '黑人为什么不回非洲呢', '拉美裔有棕皮的吧', '注意安全', '注意安全', '一定要小心。', '注意安全', '注意安全', '注意安全', '注意安全啊', '一定要注意安全，注意安全啊', '注意安全', '注意安全', '注意和别人保持距离啊', '明白人来了', '好帅', '过分了', '上网课，写作业', '做好防护，注意个人安全啊！', '经典再现', 'woc，好帅', '好帅', '冷静', '难过', '难过', '难过', '唉', '注意安全', '您帽子可以', '？？？', '这么严重', '口罩！！', '注意安全', 'wow，这小哥看上去好cool，一股子嘻哈风格', '注意安全', '注意安全啊', '绿皮书', '？？？', '红脖子！支持！！', '老外鼻子高，确实很难戴严实', '注意安全', '明明是黄种人吧？', '可怜之人必有可恨之处', '麦克风回去一定要消毒啊，别用手', '？？？？？？？？', '来者何人？', '注意安全', '保护', '哈哈哈', '唉', '太可悲了', '骑士', '太可怕了', '嗯', '白人男孩子要站起来，亚裔也一样', '帅气', '帽子好看', '？？？他们会怀疑你偷东西吗', 'freedom!!!!!!!!!!!!!!!!!!!!!!!!!!!!!', '天 黑 请 闭 眼', 'pace and love', '瓦坎达万岁', '注意安全', '？？？？', '明白人', '人心的偏见不可能消除，除非消灭人，人生来就是有偏见的', '他们在争取和平的过程中，却不知道自己的行为是暴力的', '疫情说我不背锅，你们自己国家不行别怪我', '在这个视频刷风景线的有病吗', '注意安全！', '注意安全！', '害怕', '保护', '要爆发了', '战地记者', '明白人', '推荐卷帘门', '白左、', '注意安全', '用黑色挡住了什么', '精罗狂喜', '从你的语气和表情中感受到了，确实很难', 'w', '你看，多么美丽的风景线啊', '注意安全', '这家太豪奢了', '泪目', '帽子不错', '好灵魂的回答', '通用友好手势', '说明白人的都是叛逆期吧，她也不过是利益损失，看不惯别人的其中一部分人而已', '前方无脑支持“反对者”的小学生高能', '哪里有压迫哪里就有反抗', '不是个男的吗 怎么her？谁给我科普下', '我举手你别开枪 放下手来去抢抢', '注意安全', '但是大部分是真的偷了东西啊', '？？？？？？？？？？？？', '感觉这些黑人受到教育也很好', '老特权了', '保护川普', '世界警察', '老明白人了', '保护建国同志', '说白了就是闲的蛋疼', '互摄', '没有友仔玩', '罪恶都市美国首测', '唉', '使秦复爱六国之人', '老郭，注意安全', '？？？？', '哎好心酸', '归根到底是阶级问题', '注意安全啊', '过分了', '注意安全太乱了', '口找戴好', '抢劫就应该开枪', '战地记者。', '白人也抗议，看来世界上还是有好人啊', '弹幕神经病吧。', '注意安全', '不错不错', '黄种人连上牌桌的资格都没有', '战地记者郭杰瑞', '帽子好评', '建国同志.危', '这剧情我看过', '也不排除有的人是借机闹事，乘火打劫', '有一些国家就算没有正义也很和平啊……', '鼻子露出来了（意大利戴口罩的方法）', '美国历史是不是差不多200年', '等下班在抗议', '说错了，从你们杀印第安人开始就有了。', '而且黑人确实做坏事的多，有数据的。需要注意亚裔的平等。', '旁边饿了么', '好帅！', 'what？？？？？？？？？？？？？？！！！！', '对偶句', '天黑请闭眼', '战地记者', '战地记者', '战地记者，注意安全', '？？？？？？？', '建国', '美团小哥', '泪目', '哈哈哈哈哈哈哈哈哈哈哈', '这个老哥的表达能力真好', '心酸', '狙击手报告:白色的', '穿见过…滑稽', '我是郭杰瑞', '特朗普的狗窝', '来中国啊', '演员?????', '来中国吧，让大中爱你', '女王殿下！！！！！', '王者出击啊', '？？？？？？？？', '准备战斗', '明白人', '怎么不装个电动门帘', '犹太人', '干得漂亮', 'freedom！', '你们又开始可怜别人了？？？', '？？？？', ' ,,,^^', '注意安全', '从没改变过', '哥谭市', '霉国', '我爱中国', '三连了，becare', '哪里有压迫，哪里就有反抗', '注意安全', '因为你们可以带枪啊，是你们自己选的', '注意安全', '注意安全', '美国为了下次战争要准备全民皆兵的。', '自由的气息', '心疼个毛，黑人就是懒惰的代名词', '注意安全', '口罩没带好', '大明白人', '亚裔呢', '键盘侠车在这瞎评论政治', '锅椎，你不怕他们打你吗', '喊大的那个别跑，我以为只有我看那个', '？？？？？？？？', '有病吧，谁也不会允许你把车停大马路上，这TM也算歧视？', '好惨。。。']
### word cloud plot

