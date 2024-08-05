import sys
sys.path.append(".")

from tinyrag import SentenceSplitter


def main():

    sent = """
路易八世 (巴伐利亚)\n路易八世，被称为“驼背的”或是被称为“小路易”来与他的父亲区别。维特尔斯巴赫家族成员，巴伐利亚-因戈尔施塔特公爵（1438年—1445年在位）。巴伐利亚-因戈尔施塔特公爵路易七世与第一任妻子拉马尔什伯爵约翰一世的女儿安妮的长子。\n路易八世是路易七世唯一在生的儿子，他的弟弟约翰早殇。1392年巴伐利亚公国分裂时，巴伐利亚公国由斯特凡二世的三个儿子分割为巴伐利亚-因戈尔施塔特公国、巴伐利亚-兰茨胡特公国和巴伐利亚-慕尼黑公国。在随后的几十年中，由此发展的维特尔斯巴赫家族三支系顽固地互相搏斗，彼此怀有不可调和的仇恨。在这场家庭纠纷中，巴伐利亚-因戈尔施塔特（起初是由斯特凡二世的长子斯特凡三世统治，他于1413年去世后，将公国交给儿子路易七世），而最新成立的巴伐利亚-慕尼黑公国（由斯蒂芬三世的弟弟约翰二世继承，死后由他的儿子继承恩斯特和威廉三世两兄弟共治）。最后是巴伐利亚-兰茨胡特（在斯蒂芬三世另一兄弟弗里德里希和他的儿子亨利十六世统治。）\n以权力意识的方式在这场争端中脱颖而出，通过他的妹妹法国皇后伊萨博而活跃于欧洲政治高层。试图在伊萨博皇后的帮助下增强家族的实力，安排路易七世迎娶波旁的安妮。然而，父亲与巴伐利亚-慕尼黑和巴伐利亚-兰茨胡特的堂兄的争执引起路易七世的日益关注，路易七世于1413年在父亲去世后接管巴伐利亚公国分割后的巴伐利亚-因戈尔施塔特领土。路易七世在其妻子去世后于1408年将儿子路易八世带到巴伐利亚。长达五年的旅途中的麻烦造成对他健康严重破坏，即“驼背”。\n同时，随著年龄的增长，路易八世越来越参与政府事务。1416年，他获得格赖斯巴赫伯爵的头衔，并在1420年代时，代表父亲出国访问。在1420-22年的巴伐利亚战争中，对于父亲来说战况不是很顺利，路易八世站在父亲的一方，并通过个人调解努力，使父亲获释。维特尔斯巴赫家族的施特劳宾系断嗣后，施特劳宾的继承纠纷对于因戈尔施塔特家族来说是不满意的，根据1429年普雷斯堡的仲裁，因戈尔施塔特家族只占了施特劳宾四分之一。 然而，在1439年，路易八世与巴伐利亚-慕尼黑堂兄弟缔结新协议，但该协议在1445/47年没有生效。\n父子之间的友好关系在1430年代后期恶化。原因是巴伐利亚公国的和平的观点分歧（儿子主张与父亲相反），但最重要的是父亲路易七世偏爱私生的同父异母兄弟维兰·冯·弗莱伯格而忽视合法的儿子路易八世。路易八世遂于1438年与父亲对立 ，不仅与巴伐利亚-慕尼黑公国的继承人阿尔布雷希特三世结盟，更于1443年，甚至与曾想在康斯坦斯会议杀死父亲的堂叔亨利十六世结盟。冲突导致路易八世将其父亲囚禁于多瑙河畔诺伊堡。结果，路易八世成为巴伐利亚-因戈尔施塔特公爵，但他于两年后去世，享年41岁，比他的父亲逝世还早了两年，因此无法长期居住在父亲建造的因戈尔施塔特新城堡中。\n路易八世于1441年与霍亨索伦家族勃兰登堡选侯腓特烈一世的女儿玛格丽特结婚  以换取在1420-22年的巴伐利亚战争中割让给勃兰登堡侯国的领地。二人结婚后一直没有孩子，因此，在他父亲于1447年去世后，巴伐利亚-因戈尔施塔特公国移交给亨利十六世与巴伐利亚-兰茨胡特合并。 \n家庭\n路易八世于1441年与霍亨索伦家族勃兰登堡选侯腓特烈一世的女儿玛格丽特结婚，但二人一直没有孩子。
"""
    model_id = "models/nlp_bert_document-segmentation_chinese-base"
    ss = SentenceSplitter(use_model=False, sentence_size=256, model_path=model_id)

    result = ss.split_text(sent)

    print(len(result))
    print(result)

if __name__ == "__main__":
    main()