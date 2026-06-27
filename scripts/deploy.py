import os
import click
from dotenv import load_dotenv, set_key
from ape import accounts, project, networks

load_dotenv()


@click.command()
@click.argument("account_name", required=False)
@click.option("--network", default="ethereum:sepolia:node", help="Network specifier")
@click.option(
    "--publish/--no-publish",
    default=False,
    help="Verify contract on Etherscan after deploy",
)
def cli(account_name, network, publish):
    with networks.parse_network_choice(network) as provider:
        print(f"Active Network: {provider.network.name}")

        try:
            deployer = accounts.load(account_name)
            deployer.set_autosign(True)
        except KeyError:
            print(f"Error: Account '{account_name}' is not found in Ape.")
            return

        print(f"Deploying contracts using account: {deployer.address}")

        my_token = deployer.deploy(project.TebakAngkaCoin, deployer.address, publish=publish)
        print(f"TebakAngkaCoin successfully deployed to: {my_token.address}")
        set_key(".env", "TEBAK_ANGKA_COIN_ADDRESS", my_token.address)
        
        my_nft = deployer.deploy(
            project.TebakAngkaNFT, deployer.address, publish=publish
        )
        print(f"TebakAngkaNFT successfully deployed to: {my_nft.address}")
        set_key(".env", "TEBAK_ANGKA_NFT_ADDRESS", my_nft.address)

        game = deployer.deploy(
            project.TebakAngka, my_token.address, my_nft.address, publish=publish
        )
        print(f"TebakAngka Game successfully deployed to: {game.address}")
        set_key(".env", "TEBAK_ANGKA_ADDRESS", game.address)

        if publish:
            print(f"Contracts verified on Etherscan!")
