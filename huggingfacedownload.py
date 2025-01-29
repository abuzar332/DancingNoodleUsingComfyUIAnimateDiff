pip install huggingface_hub[hf_transfer]
pip install hf_transfer





huggingface-cli login --token YOURTOKEN
export HF_HUB_ENABLE_HF_TRANSFER=1


huggingface-cli download OedoSoldier/detail-tweaker-lora --local-dir ./ComfyUI/models/loras/



huggingface-cli download h94/IP-Adapter --local-dir ./ComfyUI/models/ipadapter/


huggingface-cli download wangfuyun/AnimateLCM --local-dir ./ComfyUI/models/animatediff_models/


huggingface-cli download laion/CLIP-ViT-H-14-laion2B-s32B-b79K --local-dir ./ComfyUI/models/clip_vision/

 
mv ./ComfyUI/models/clip_vision/model.safetensors ./ComfyUI/models/clip_vision/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors



huggingface-cli download monster-labs/control_v1p_sd15_qrcode_monster --local-dir ./ComfyUI/models/controlnet/

huggingface-cli download lllyasviel/control_v11p_sd15_lineart --local-dir ./ComfyUI/models/controlnet/


mv ./ComfyUI/models/controlnet/diffusion_pytorch_model.safetensors ./ComfyUI/models/controlnet/control_v11p_sd15_lineart.safetensors

huggingface-cli download gemasai/4x_NMKD-Siax_200k --local-dir ./ComfyUI/models/upscale_models/


cd ComfyUI/custom_nodes/comfyui_layerstyle/

git clone https://huggingface.co/briaai/RMBG-1.4

cd /workspace

huggingface-cli download briaai/RMBG-1.4 --local-dir ./ComfyUI/custom_nodes/comfyui_layerstyle/RMBG-1.4/







