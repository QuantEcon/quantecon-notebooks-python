import os
from pathlib import Path
# filenames=[
#     'oop_intro',
#     'python_oop',
#     'need_for_speed',
#     'numpy',
#     'matplotlib',
#     'scipy',
#     'numba',
#     'parallelization',
#     'pandas',
#     'writing_good_code',
#     'python_advanced_features',
#     'debugging'
# ]

# filenames = ['', '', 'index_toc.html#Table-of-Contents', 'about_lectures.html', 'index_tools_and_techniques.html', 'orth_proj.html', 'stationary_densities.html', 'muth_kalman.html', 'discrete_dp.html', 'index_lq_control.html', 'cons_news.html', 'smoothing.html', 'smoothing_tax.html', 'robustness.html', 'markov_jump_lq.html', 'tax_smoothing_1.html', 'tax_smoothing_2.html', 'tax_smoothing_3.html', 'lqramsey.html', 'index_multi_agent_models.html', 'rob_markov_perf.html', 'arellano.html', 'matsuyama.html', 'coase.html', 'index_hs_recursive_models.html', 'hs_recursive_models.html', 'growth_in_dles.html', 'lucas_asset_pricing_dles.html', 'irfs_in_hall_model.html', 'permanent_income_dles.html', 'rosen_schooling_model.html', 'cattle_cycles.html', 'hs_invertibility_example.html', 'index_classic_linear_models.html', 'von_neumann_model.html', 'index_time_series_models.html', 'arma.html', 'estspec.html', 'additive_functionals.html', 'lu_tricks.html', 'classical_filtering.html', 'index_asset_pricing.html', 'lucas_model.html', 'black_litterman.html', 'BCG_complete_mkts.html', 'BCG_incomplete_mkts.html', 'index_dynamic_programming_squared.html', 'dyn_stack.html', 'calvo.html', 'opt_tax_recur.html', 'amss.html', 'amss2.html', 'amss3.html', 'chang_ramsey.html', 'chang_credible.html', 'zreferences.html']
filenames = ['', '', 'index_toc.html#Table-of-Contents', 'about_lectures.html', 'index_tools_and_techniques.html', 'geom_series.html', 'multi_hyper.html', 'sir_model.html', 'linear_algebra.html', 'complex_and_trig.html', 'lln_clt.html', 'heavy_tails.html', 'multivariate_normal.html', 'time_series_with_matrices.html', 'index_intro_dynam.html', 'scalar_dynam.html', 'ar1_processes.html', 'finite_markov.html', 'inventory_dynamics.html', 'linear_models.html', 'samuelson.html', 'kesten_processes.html', 'wealth_dynamics.html', 'kalman.html', 'short_path.html', 'cass_koopmans_1.html', 'cass_koopmans_2.html', 'index_search.html', 'mccall_model.html', 'mccall_model_with_separation.html', 'mccall_fitted_vfi.html', 'mccall_correlated.html', 'career.html', 'jv.html', 'index_savings_growth.html', 'cake_eating_problem.html', 'cake_eating_numerical.html', 'optgrowth.html', 'optgrowth_fast.html', 'coleman_policy_iter.html', 'egm_policy_iter.html', 'ifp.html', 'ifp_advanced.html', 'index_information.html', 'odu.html', 'likelihood_ratio_process.html', 'wald_friedman.html', 'exchangeable.html', 'likelihood_bayes.html', 'navy_captain.html', 'index_lq_control.html', 'lqcontrol.html', 'perm_income.html', 'perm_income_cons.html', 'lq_inventories.html', 'index_multi_agent_models.html', 'schelling.html', 'lake_model.html', 'rational_expectations.html', 're_with_feedback.html', 'markov_perf.html', 'uncertainty_traps.html', 'aiyagari.html', 'index_asset_pricing.html', 'markov_asset.html', 'harrison_kreps.html', 'index_data_and_empirics.html', 'pandas_panel.html', 'ols.html', 'mle.html', 'zreferences.html']
start = int(input('enter new_row: '))
for file in filenames:
    notebook = file.split('.')[0]+'.ipynb'
    path = Path(notebook)
    print(path, path.is_file())
    if path.is_file():
        new_path = f'Basic/{start:02}-{notebook}'
        path.rename(new_path)
        print(new_path)
        start+=1