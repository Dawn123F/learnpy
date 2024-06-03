
from openai import OpenAI

client = OpenAI(base_url='https://api.aigc369.com/v1')

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "user", "content": "生成一份购物清单"}
  ],
  max_tokens=1000,   # 控制大模型回复的最大篇幅
  temperature=0.1,   # 控制ai回答的创造性
 # top_p=0.5  # 控制ai回答的创造性 控制回复内容的概率子集
 #frequency_penalty=2, #减少回答中重复的词的生成概率 值为-2 到 2 推荐设置成 0到1之间
 presence_penalty=2 # 让生成内容包含更多的新词
)

# 通过GPT变现，用户可以将自己的写作才能转化为实际收入。GPT是一种先进的人工智能技术，
# 可以生成高质量的文本内容。通过将自己的写作作为输入，GPT可以生成各种类型的文本
# ，包括文章、故事、甚至代码。用户可以将这些生成的内容出售给其他用户或者发布在社交平台上获取收入
# 。这种变现方式不仅能够让用户赚取额外的收入，还可以帮助他们提升写作能力和拓展创意思维
# 。通过GPT变现，写作不再只是一种爱好，而是一种可以创造价值的技能。

print(response.choices[0].message.content)