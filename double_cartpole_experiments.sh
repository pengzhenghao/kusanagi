#!//usr/bin/env bash

#OPTS="-r -d 1 -o ${HOME}/.kusanagi/dcp_results"
OPTS="-o ${HOME}/.kusanagi/dcp_results"
EXPERIMENT_OPTS="-k n_opt 50 -k n_rnd 2"
MCPILCO_OPTS="-k mc_samples 100 -k heteroscedastic_dyn True -k mm_state True -k mm_cost False -k noisy_policy_input True -k noisy_cost_input False"
OPTIMZER_OPTS="-k max_evals 1000 -k learning_rate 1e-4 -k polyak_averaging None -k clip_gradients 1.0"
#python examples/PILCO/double_cartpole_learn.py -e 1 -n dcp_pilco_ssgp_rbfp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
#python examples/PILCO/double_cartpole_learn.py -e 3 -n dcp_mcpilco_dropoutd_rbfp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
#python examples/PILCO/double_cartpole_learn.py -e 5 -n dcp_mcpilco_lndropoutd_rbfp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
python examples/PILCO/double_cartpole_learn.py -e 8 -n dcp_mcpilco_lndropoutd_dropoutp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
python examples/PILCO/double_cartpole_learn.py -e 7 -n dcp_mcpilco_dropoutd_dropoutp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
python examples/PILCO/double_cartpole_learn.py -e 6 -n dcp_mcpilco_lndropoutd_mlpp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
python examples/PILCO/double_cartpole_learn.py -e 4 -n dcp_mcpilco_dropoutd_mlpp ${OPTS} ${EXPERIMENT_OPTS} ${MCPILCO_OPTS} ${OPTIMZER_OPTS}
