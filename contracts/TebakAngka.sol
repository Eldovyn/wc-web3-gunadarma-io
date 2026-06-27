// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.27;

interface MTKCoin {
    function mint(address to, uint256 amount) external;
}

interface TebakAngkaNFT {
    function mint(address to, string memory tokenURI) external;
}

contract TebakAngka {
    MTKCoin public tokenContract;
    TebakAngkaNFT public nftContract;

    struct PlayerInfo {
        uint256 wins;
        uint256 losses;
    }

    mapping(address => PlayerInfo) public playerStats;

    event GuessMode(
        address indexed player,
        uint8 guess,
        uint8 correctNumber,
        bool won
    );

    constructor(address _tokenContract, address _nftContract) {
        tokenContract = MTKCoin(_tokenContract);
        nftContract = TebakAngkaNFT(_nftContract);
    }

    function guess(
        uint8 number,
        string memory winURI,
        string memory loseURI
    ) external {
        require(number >= 1 && number <= 5, "angka harus di anatara 1 dan 5");

        uint8 correctNumber = uint8(
            uint256(
                keccak256(
                    abi.encodePacked(
                        block.timestamp,
                        block.prevrandao,
                        msg.sender
                    )
                )
            ) % 5
        ) + 1;

        bool won = (number == correctNumber);

        if (won) {
            playerStats[msg.sender].wins++;

            tokenContract.mint(msg.sender, 10 * 10 ** 18);

            nftContract.mint(msg.sender, winURI);
        } else {
            playerStats[msg.sender].losses++;
            nftContract.mint(msg.sender, loseURI);
        }

        emit GuessMode(msg.sender, number, correctNumber, won);
    }
}
