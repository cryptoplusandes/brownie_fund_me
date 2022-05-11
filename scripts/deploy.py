# from brownie import accounts
from brownie import FundMe, MockV3Aggregator, network, config

from scripts.helpful_scripts import (
    get_account,
    deploy_mocks,
    LOCAL_BLOCKCHAIN_ENVIRONMENTS,
)

# from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contrast

    # if we are on a persistent network like rinkeby, use the address
    # otherwise, deploy mocks
    # if network.show_active() != "development":
     if network.show_active() not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network.show_active()][
            "eth_usd_price_feed"
        ]
    else:
        # print(f"The active network is {network.show_active()}")
        # print("Deployind Mocks...")
        # if len(MockV3Aggregator) <= 0:
        #    MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether") {"from": account})
        # # mock_aggregator = MockV3Aggregator.deploy(18, Web3.toWei(2000, "ether") {"from": account})
        # # 18, 2000000000000000000000, {"from": account}
        # # price_feed_address = mock_aggregator.address
        # print("Mocks Deployed!")
        # price_feed_address = MockV3Aggregator[-1].address
        # print("Mocks Deployed!")
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address
    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to{fund_me.address}")
    return fund_me


# def deploy_simple_storage():
#     # account = accounts[0]
#     # print(account)
#     account = accounts.load(feecodecamp - account)
#     print(account)


def main():
    deploy_fund_me()
