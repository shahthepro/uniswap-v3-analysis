enable_rebalancer = True
deposit_liquidities = [
  # (50000, 50000),
  (500000, 500000),
  # (2500000, 2500000),
]
tick_ranges = [1, 2, 4, 8, 10, 100]
rebase_frequencies = [
  0,
  # 10,
  # 100,
]

scenarios = []

for (usdc_amount, usdt_amount) in deposit_liquidities:
  for tick_range in tick_ranges:
    for frequency in rebase_frequencies:
      scenarios.append({
        "address": "0xsim_{}_{}_{}_{}".format(tick_range, frequency, usdc_amount, usdt_amount),
        "usdc_amount": usdc_amount,
        "usdt_amount": usdt_amount,
        "deposit_after": 14236000,
        "withdraw_before": 0,
        "lower_tick": 1 - (tick_range * 0.0001),
        "upper_tick": 1 + (tick_range * 0.0001),
        "enable_rebalancer": enable_rebalancer,
        "rebalance_frequency": frequency,
        "target_tick_range": tick_range
      })

# scenarios = [
#   # Rebalance Frequency: 0, 
#   {
#     "address": "0xr1", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.9999, # in USD, $1 denomination
#     "upper_tick": 1.0001, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 1,
#   },
#   {
#     "address": "0xr2", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.9998, # in USD, $1 denomination
#     "upper_tick": 1.0002, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 2,
#   },
#   {
#     "address": "0xr3", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.9996, # in USD, $1 denomination
#     "upper_tick": 1.0004, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 4,
#   },
#   {
#     "address": "0xr4", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.9992, # in USD, $1 denomination
#     "upper_tick": 1.0008, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 8,
#   },
#   {
#     "address": "0xr5", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.999, # in USD, $1 denomination
#     "upper_tick": 1.001, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 10,
#   },
#   {
#     "address": "0xr6", # any string works
#     "usdc_amount": 500000, # USDC to deposit, in dollar denomination
#     "usdt_amount": 500000, # USDT to deposit, in dollar denomination
#     "deposit_after": 14236000, # Block to deposit from
#     "withdraw_before": 0, # Block to withdraw from
#     "lower_tick": 0.99, # in USD, $1 denomination
#     "upper_tick": 1.01, # in USD, $1 denomination
#     "enable_rebalancer": True, # If true, tries to chase the active
#     "rebalance_frequency": 0, # How many blocks to wait before rebalancing
#     "target_tick_range": 100,
#   },

  # # Rebalance Frequency: 10, 
  # {
  #   "address": "0xr11", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9999, # in USD, $1 denomination
  #   "upper_tick": 1.0001, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 1,
  # },
  # {
  #   "address": "0xr12", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9998, # in USD, $1 denomination
  #   "upper_tick": 1.0002, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 2,
  # },
  # {
  #   "address": "0xr13", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9996, # in USD, $1 denomination
  #   "upper_tick": 1.0004, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 4,
  # },
  # {
  #   "address": "0xr14", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9992, # in USD, $1 denomination
  #   "upper_tick": 1.0008, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 8,
  # },
  # {
  #   "address": "0xr15", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.999, # in USD, $1 denomination
  #   "upper_tick": 1.001, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 10,
  # },
  # {
  #   "address": "0xr16", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.99, # in USD, $1 denomination
  #   "upper_tick": 1.01, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 10, # How many blocks to wait before rebalancing
  #   "target_tick_range": 100,
  # },

  # # Rebalance Frequency: 100, 
  # {
  #   "address": "0xr101", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9999, # in USD, $1 denomination
  #   "upper_tick": 1.0001, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 1,
  # },
  # {
  #   "address": "0xr102", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9998, # in USD, $1 denomination
  #   "upper_tick": 1.0002, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 2,
  # },
  # {
  #   "address": "0xr103", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.99, # in USD, $1 denomination
  #   "upper_tick": 1.01, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 4,
  # },
  # {
  #   "address": "0xr104", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9992, # in USD, $1 denomination
  #   "upper_tick": 1.0008, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 8,
  # },
  # {
  #   "address": "0xr105", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.999, # in USD, $1 denomination
  #   "upper_tick": 1.001, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 10,
  # },
  # {
  #   "address": "0xr106", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.99, # in USD, $1 denomination
  #   "upper_tick": 1.01, # in USD, $1 denomination
  #   "enable_rebalancer": True, # If true, tries to chase the active
  #   "rebalance_frequency": 100, # How many blocks to wait before rebalancing
  #   "target_tick_range": 100,
  # },

  # # Non-rebalancing ones
  # {
  #   "address": "0xf1", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9999, # in USD, $1 denomination
  #   "upper_tick": 1.0001, # in USD, $1 denomination
  # },
  # {
  #   "address": "0xf2", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9998, # in USD, $1 denomination
  #   "upper_tick": 1.0002, # in USD, $1 denomination
  # },
  # {
  #   "address": "0xf3", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9996, # in USD, $1 denomination
  #   "upper_tick": 1.0004, # in USD, $1 denomination
  # },
  # {
  #   "address": "0xf4", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.9992, # in USD, $1 denomination
  #   "upper_tick": 1.0008, # in USD, $1 denomination
  # },
  # {
  #   "address": "0xf5", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.999, # in USD, $1 denomination
  #   "upper_tick": 1.001, # in USD, $1 denomination
  # },
  # {
  #   "address": "0xf6", # any string works
  #   "usdc_amount": 500000, # USDC to deposit, in dollar denomination
  #   "usdt_amount": 500000, # USDT to deposit, in dollar denomination
  #   "deposit_after": 14236000, # Block to deposit from
  #   "withdraw_before": 0, # Block to withdraw from
  #   "lower_tick": 0.99, # in USD, $1 denomination
  #   "upper_tick": 1.01, # in USD, $1 denomination
  # },
# ]
