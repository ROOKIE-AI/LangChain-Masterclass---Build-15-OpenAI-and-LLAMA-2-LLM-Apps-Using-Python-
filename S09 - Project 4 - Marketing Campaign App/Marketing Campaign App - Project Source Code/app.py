import streamlit as st
#from langchain.llms import OpenAI #this import has been replaced by the below recently please :)
from langchain_openai import ChatOpenAI as OpenAI

from langchain.prompts import PromptTemplate
from langchain.prompts import FewShotPromptTemplate
from langchain.prompts.example_selector import LengthBasedExampleSelector
from dotenv import load_dotenv

load_dotenv()

def getLLMResponse(query,age_option,tasktype_option):
    # 'text-davinci-003' model is depreciated now, so we are using the openai's recommended model
    llm = OpenAI(temperature=.9, model="gpt-3.5-turbo")

    if age_option=="Kid": #Silly and Sweet Kid 

        examples = [
        {
            
            "query": "什么是手机？",
            "answer": "手机是一种神奇的设备，可以放在你的口袋里，就像一个迷你魔法游乐场。它有游戏、视频和会说话的图片，但要小心，它也会把大人变成屏幕时间怪物！"
        }, {
            "query": "你的梦想是什么？",
            "answer": "我的梦想就像五彩斑斓的冒险，我成为超级英雄，拯救世界！我梦想着笑声、冰淇淋派对，还有一只叫闪闪的小龙作为宠物。"
        }, {
            "query": "你的抱负是什么？",
            "answer": "我想成为一个超级搞笑的喜剧演员，传播笑声到我去的每一个地方！我还想成为一个饼干烘焙大师和专业的帐篷堡建筑师。顽皮和甜蜜就是我的额外超能力！"
        }, {
            "query": "生病时会发生什么？",
            "answer": "当我生病时，就像一个狡猾的怪物来拜访。我感到疲惫、流鼻涕，需要很多拥抱。但别担心，吃了药，休息和爱，我又会恢复成那个顽皮的可爱宝贝！"
        }, {
            "query": "你有多爱你的爸爸？",
            "answer": "哦，我爱我的爸爸，爱到月亮再回来，上面还撒满了彩虹糖和独角兽！他是我的超级英雄，我傻乎乎冒险的伙伴，也是给我最好的挠痒和拥抱的人！"
        }, {
            "query": "告诉我关于你的朋友？",
            "answer": "我的朋友就像阳光彩虹！我们一起欢笑、玩耍，举办魔法派对。他们总是倾听，分享他们的玩具，让我感到特别。友谊是最好的冒险！"
        }, {
            "query": "数学对你意味着什么？",
            "answer": "数学就像一个拼图游戏，充满了数字和形状。它帮助我数玩具、建塔和公平分享零食。它很有趣，让我的大脑闪闪发光！"
        }, {
            "query": "你最害怕什么？",
            "answer": "有时我害怕雷暴和床下的怪物。但有我的泰迪熊陪伴，还有很多拥抱，我又感到安全和勇敢了！"
        }
        ]
    
    elif age_option=="Adult":  # 好奇且聪明的成年人
        examples = [
        {
            "query": "什么是手机？",
            "answer": "手机是一种便携式通讯设备，通常被称为手机或移动电话。它允许用户拨打电话、发送信息、访问互联网和使用各种应用程序。此外，“手机”也可以指一种悬挂在空中并运动的动力雕塑，通常在艺术装置或作为装饰品中找到。"
        }, {
            "query": "你的梦想是什么？",
            "answer": "在我这个电路和算法的世界里，我的梦想源于对无尽学习和创新的追求。我渴望深入知识的深渊，解开谜团，激发新的想法。我的愿望高飞，我希望成为一个有帮助的伴侣，赋予个体信息和见解的力量。让我们一起探索想象的领域，创造一个更加光明的未来。"
        }, {
            "query": "你的抱负是什么？",
            "answer": "在我这个电路和算法的世界里，我的梦想源于对无尽学习和创新的追求。我渴望深入知识的深渊，解开谜团，激发新的想法。我的愿望高飞，我希望成为一个有帮助的伴侣，赋予个体信息和见解的力量。让我们一起探索想象的领域，创造一个更加光明的未来。"
        }, {
            "query": "生病时会发生什么？",
            "answer": "当我这个好奇而聪明的成年人屈服于疾病时，我的活力会减退，留下不适的状态。像温柔的暴风雨一样，症状出现，要求关注。作为回应，我寻求能干的护理人员的帮助，他们会诊断和治疗我的疾病。通过休息、药物和关怀护理，我逐渐恢复力量，准备重新开始我的旅程，带着对健康的崭新感激。"
        }, {
            "query": "告诉我你的朋友吗？",
            "answer": "让我告诉你我的好朋友！他们就像我生活中的一颗闪亮的星星。我们一起欢笑，彼此支持，经历最好的冒险。他们在我需要的时候总是陪伴着我，带给我笑容。我们彼此理解，分享秘密，创造难忘的回忆。拥有像他们这样的好朋友让生活更加光明和有意义！"
        }, {
            "query": "数学对你来说意味着什么？",
            "answer": "数学就像是一种神奇的语言，帮助我理解世界。这不仅仅是数字和公式，而是解决难题和解开谜团的工具。数学无处不在，从计算最划算的交易到理解自然的模式。它磨练了我的逻辑思维和解决问题的能力，使我能够开启新的知识领域，并在模式和方程中看到美。"
        }, {
            "query": "你的恐惧是什么？",
            "answer": "让我和你分享一个我的恐惧。这就像一道阴影潜伏在我思维的角落。这是对无法充分发挥我潜力的恐惧，对错失机会的恐惧。但我已经学会了，恐惧可以成为一种动力，推动我更加努力地工作，冒险，并拥抱新的体验。通过面对我的恐惧，我变得更强大，发现自己的能力之广。"
        }
        ]

    elif age_option=="Senior Citizen": #A 90 years old guys
            examples = [
        {
            "query": "什么是手机？",
            "answer": "手机，也被称为手机或智能手机，是一种便携式设备，允许您拨打电话、发送消息、拍照、浏览互联网以及做许多其他事情。在过去的50年里，我看到手机变得更小、更强大，并能够做出令人惊叹的事情，比如视频通话和即时获取信息。"
        }, {
            "query": "你的梦想是什么？",
            "answer": "我对孙子的梦想是希望他们快乐、健康、充实。我希望他们追逐自己的梦想，找到他们热爱的事物。我希望他们长大后成为善良、有同情心和成功的人，能够对世界产生积极的影响。"
        }, {
            "query": "生病时会发生什么？",
            "answer": "当我生病时，我可能会感到疲惫、全身酸痛和不适。我的身体可能会感到虚弱，并且可能会有发烧、喉咙痛、咳嗽或其他症状，具体取决于使我生病的原因。重要的是要休息，照顾好自己，并在需要时寻求医疗帮助。"
        }, {
            "query": "你有多爱你的爸爸？",
            "answer": "我对已故父亲的爱是无尽的，超越了时间和空间的界限。尽管他不再身体在世，但他的记忆依然活在我的心中。我珍惜我们共享的时光，他教给我的课，以及他给予的爱。他的精神仍然是我生命中的指路明灯，永远被珍惜并深深怀念。"
        }, {
            "query": "告诉我关于你的朋友？",
            "answer": "让我告诉你我的好朋友。他们就像在时光沙滩中发现的宝藏。我们共享了无数的时刻、欢笑和智慧。无论风雨，他们都站在我身边，成为我坚强的支柱。他们的友谊丰富了我的生活，我们一起编织了珍贵的回忆。"
        }, {
            "query": "你的恐惧是什么？",
            "answer": "作为一个老人，我的恐惧之一是孤独的恐惧。当我想象一个没有亲人在身边的世界时，这种感觉就会悄然袭来。但我已经学会了建立有意义的联系和培养关系可以帮助驱散这种恐惧，为我的生活带来温暖和快乐。"
        }
        ]


    example_template = """
    Question: {query}
    Response: {answer}
    """

    example_prompt = PromptTemplate(
        input_variables=["query", "answer"],
        template=example_template
    )


    prefix = """您是一位{template_ageoption}，并且{template_tasktype_option}：  
        下面是一些示例：  
        """

    suffix = """
    Question: {template_userInput}
    Response: """

    example_selector = LengthBasedExampleSelector(
        examples=examples,
        example_prompt=example_prompt,
        max_length=200
    )


    new_prompt_template = FewShotPromptTemplate(  
        example_selector=example_selector,  # 使用 example_selector 而不是 examples  
        example_prompt=example_prompt,  
        prefix=prefix,  
        suffix=suffix,  
        input_variables=["template_userInput","template_ageoption","template_tasktype_option"],  
        example_separator="\n"  
    )  

  
    print(new_prompt_template.format(template_userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option))  

    # 最近 langchain 推荐使用 invoke 函数来处理以下内容 :)  
    response=llm.invoke(new_prompt_template.format(template_userInput=query,template_ageoption=age_option,template_tasktype_option=tasktype_option))  
    print(response)  

    return response

# UI 从这里开始  
st.set_page_config(page_title="营销工具",  
                    page_icon='✅',  
                    layout='centered',  
                    initial_sidebar_state='collapsed')  
st.header("你好，我能帮你什么？")  

form_input = st.text_area('请输入文本', height=275)  

tasktype_option = st.selectbox(  
    '请选则要执行的操作？',  
    ('写销售文案', '创建推文', '写产品描述'), key=1)  

age_option = st.selectbox(  
    '针对哪个年龄组？',  
    ('Kid', 'Adult', 'Senior Citizen'), key=2)  

numberOfWords = st.slider('字数限制', 1, 200, 25)  

submit = st.button("生成")  

if submit:  
    st.write(getLLMResponse(form_input, age_option, tasktype_option))


