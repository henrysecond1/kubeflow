# This file is only intended for development purposes
from kubeflow.kubeflow.cd import base_runner

base_runner.main(component_name="notebook_controller",
                 workflow_name="nb-c-build")
