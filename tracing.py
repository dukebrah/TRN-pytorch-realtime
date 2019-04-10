import torch
import torchvision
from models import TSN

# An instance of your model.
net = TSN(27,
          8,
          'Ecc',
          base_model='BNInception',
          consensus_type='TRNmultiscale',
          img_feature_dim=256, print_spec=False)


# An example input you would normally provide to your model's forward() method.
#example = torch.rand(1, 3, 224, 224)

# Use torch.jit.trace to generate a torch.jit.ScriptModule via tracing.
traced_script_module = torch.jit.trace(model, example)
torch.j