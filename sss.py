import streamlit as st
import time
from background import BackgroundCSSGenerator

st.set_page_config(
    page_title="Snowflake Arctic Overview",
    page_icon="❄️",
    layout="wide"
)

img1_path = r"download.jpg"
img2_path = r"Gemini_Generated_Image (2).jpg"
background_generator = BackgroundCSSGenerator(img1_path, img2_path)
page_bg_img = background_generator.generate_background_css()
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("❄️ SnowFlake Arctic : An Enterprise Grade Open Source LLM ❄️")
st.divider()

st.header("About 'Snowflake Arctic' ❄️")
st.write("Snowflake Arctic, developed by the Snowflake AI Research Team, represents a significant advancement in large language models (LLMs) tailored specifically for enterprise applications. It stands out for its innovative hybrid architecture, cost-effective training approach, and commitment to openness. ❄️⛄")
st.divider()

st.header("Key Features ✨:")
st.write("- ❄️ Hybrid Architecture: Combines a dense transformer model with a residual MoE (Mixture of Experts) MLP, resulting in a unique and efficient model design.")
st.write("- ❄️ Cost-Effective Training: Trained with a budget of under $2 million, significantly lower compared to other models like GPT-4, making it accessible to a broader range of users.")
st.write("- ❄️ Open-Source Nature: Licensed under the Apache 2.0 license, providing access to weights, code, data recipes, and research insights, fostering collaboration and innovation in the AI community.")
st.divider()

st.header("Model Architecture and Functionality 🏗️")
st.write("Snowflake Arctic's architecture and functionality set it apart from traditional large language models.")
st.write("")
st.write("")

st.subheader("Hybrid Architecture ❄️:")
st.write("- 🧊 Dense Transformer Model: Utilizes a dense transformer architecture, known for its scalability and performance in processing large amounts of data.")
st.write("- ⛄ Residual MoE MLP: Incorporates a Mixture of Experts model, enhancing performance by leveraging multiple specialized experts for different tasks.")
st.write("")
st.write("")
st.write("")
st.write("")
coll1,coll3 = st.columns([1,1])
with coll1:
 st.image('5.png',caption='Standard MOE Architecture',use_column_width=True)
with coll3:
 st.write("")
 st.write("")
 st.write("")
 st.image('dpt.jpg',caption='DPT',use_column_width=True)
   
st.divider()

st.subheader("Efficient Design ⚙:")
st.write("- ❄️ Parameter Configuration: Boasts 480 billion parameters, including 128 fine-grained experts, selected using a top-2 gating mechanism, optimizing resource utilization and model quality.")
st.write("- ❄️ Active Parameter Selection: Employs a top-2 gating mechanism, ensuring that only 17 billion parameters are active at any given time, further enhancing efficiency and performance.")
st.divider()

st.subheader("Training Process 🏃:")
st.write("- ❄️ Data and Training: Trained on 3.5T enterprise tokens, with a focus on enterprise-specific benchmarks and tasks, ensuring high performance in real-world applications.")
st.write("- ❄️ Resource Optimization: Leverages efficient parameter selection and model architecture to maximize performance while minimizing computational resources.")
st.divider()

st.header("Training and Performance 📈")
st.write("Snowflake Arctic's training process and performance metrics demonstrate its effectiveness compared to other LLMs.")
st.write("")
st.write("")

st.subheader("Training Efficiency 📈:")
st.write("- 🏂 Cost-Effective Training: Achieves high-quality results with a relatively low training budget, making it accessible to enterprises of all sizes.")
st.write("- 🏂 Optimized Resource Utilization: Leverages efficient parameter selection and model architecture to maximize performance while minimizing computational resources.")
st.divider()

st.subheader("Performance Metrics 📊:")
st.write("- 🏂 Benchmark Comparisons: Arctic exceeds or matches the performance of Llama 3 in various enterprise-specific tasks, including SQL generation, coding assistance, and instruction following.")
st.write("- 🏂 Resource Efficiency: Achieves comparable or superior performance while using fewer computational resources and training budget compared to other models.")
st.divider()

st.header("Comparison with Other LLMs 📊")
st.write("Snowflake Arctic's performance and efficiency stand out when compared to other large language models in the field ☃️")
st.write("")
st.write("")

st.subheader("Comparative Analysis ❄️:")
st.write("- ❄️ Performance Benchmarks: Arctic exceeds or matches the performance of Llama 3, GPT-3, and other leading models in enterprise tasks, showcasing its efficacy in real-world applications.")
st.write("- ❄️ Resource Utilization: Demonstrates superior efficiency and cost-effectiveness, making it an attractive option for businesses seeking to deploy AI solutions at scale.")
st.write("- ❄️ Training Budget: Significantly lower training cost compared to other models, enabling enterprises to achieve high-quality results without exorbitant investment.")
col1,col2=st.columns([1,1])
with col1:
    st.image('1.jpg', use_column_width=True)
with col2:
    st.write("")
    st.write("")
    st.image('2.jpg', use_column_width=True)

st.divider()

st.subheader("Active Parameter Selection ❄️")
st.write("Snowflake Arctic's utilization of active parameters enhances its efficiency and performance.")

st.write("- ❄️ Top-2 Gating Mechanism: Parameters are chosen using a top-2 gating mechanism, which selects the most relevant experts for a given input, further enhancing the model's efficiency and effectiveness.")
st.write("- ❄️ Resource Efficiency: By activating a subset of parameters based on input context, Arctic minimizes computational overhead while maintaining high-quality outputs, making it suitable for deployment in resource-constrained environments.")
st.divider()
st.header("Future Directions and Impact 🌟")
st.write("Snowflake Arctic's innovative approach and promising performance have significant implications for the future of AI technology and enterprise applications.")
st.write("")
st.write("")

st.subheader("Potential Impact ❄️:")
st.write("- ❄️ Accessibility: Empowers businesses with accessible and cost-effective AI solutions, driving innovation and efficiency across various industries.")
st.write("- ❄️ Innovation: Fosters collaboration and knowledge sharing within the AI community, contributing to the evolution of AI technologies and practices.")
st.write("- ❄️ Industry Applications: Enables a wide range of applications in industries such as retail, finance, healthcare, and more, revolutionizing business operations and customer experiences.")
st.divider()
st.subheader("Future Developments 🌟:")
st.write("- ❄️ Continued Improvements: Enhancements in model performance, efficiency, and scalability, expanding its capabilities and applications in enterprise AI.")
st.write("- ❄️ Enhanced Integration: Integration with Snowflake's ecosystem and other platforms, facilitating seamless deployment and adoption in diverse business environments.")
st.divider()
st.subheader("Recommended Setup for Full Performance 💻")
st.write("Due to the model size, they recommend using a single 8xH100 instance of your favorite cloud provider such as: AWS p5.48xlarge, Azure ND96isr")
st.divider()
st.subheader("Try It Out! 🌐")
st.write("Check this Streamlit page hosted using the Replicate API: [Snowflake Arctic Streamlit Page](https://arctic.streamlit.app/)")
st.divider()
st.subheader("Learn More ❄️:")
st.write("- ❄️ [Snowflake Arctic: An Open, Efficient Foundation for Language Models](https://www.snowflake.com/blog/arctic-open-efficient-foundation-language-models-snowflake/)")
st.write("- ❄️ [Snowflake Arctic Model on Hugging Face](https://huggingface.co/Snowflake/snowflake-arctic-instruct)")

st.divider()
st.header("Conclusion 🎉")
st.write("Snowflake Arctic emerges as a leading enterprise-focused large language model, offering unparalleled performance, efficiency, and openness. Its innovative hybrid architecture, cost-effective training approach, and versatile applications position it as a transformative asset for businesses seeking to harness the power of AI for competitive advantage and innovation in the enterprise space.")

while True:
    st.snow()
    time.sleep(25)
