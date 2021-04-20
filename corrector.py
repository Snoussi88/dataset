from transformers import AutoTokenizer, AutoModelWithLMHead, AutoModelForCausalLM
import torch
if torch.cuda.is_available():
    device = torch.device("cuda")
    
else :
    device = "cpu"


tokenizer = AutoTokenizer.from_pretrained("salesken/grammar_correction")  
model = AutoModelForCausalLM.from_pretrained("salesken/grammar_correction").to(device)

input_query="i visited you tomorrow"
query= "<|startoftext|> " + input_query + " ~~~"


input_ids = tokenizer.encode(query.lower(), return_tensors='pt').to(device)
sample_outputs = model.generate(input_ids,
                                do_sample=True,
                                num_beams=1, 
                                max_length=128,
                                temperature=0.9,
                                top_p= 0.7,
                                top_k = 5,
                                num_return_sequences=3)
corrected_sentences = []
for i in range(len(sample_outputs)):
    r = tokenizer.decode(sample_outputs[i], skip_special_tokens=True).split('||')[0]
    r = r.split('~~~')[1]
    if r not in corrected_sentences:
        corrected_sentences.append(r)

print(corrected_sentences)