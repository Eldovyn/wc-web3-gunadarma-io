// SPDX-Licence-Identifier: MIT
pragma solidity ^0.8.27;

import {ERC721} from "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import {Ownable} from "@openzeppelin/contracts/access/Ownable.sol";
import {ERC721URIStorage} from "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";

contract TebakAngkaNFT is ERC721, ERC721URIStorage, Ownable {
    uint256 public nextTokenId;

    struct NFTMetaData {
        address creator;
        uint256 timestamp;
    }

    mapping(uint256 => NFTMetaData) public nftDetails;

    constructor(
        address initialOwner
    ) ERC721("TebakAngka NFT", "TAN") Ownable(initialOwner) {}

    function mint(address to, string memory tokenURI) public {
        uint256 tokenId = nextTokenId;
        _safeMint(to, tokenId);
        _setTokenURI(tokenId, tokenURI);

        nftDetails[tokenId] = NFTMetaData({
            creator: to,
            timestamp: block.timestamp
        });
    }

    function getNFTDetails(
        uint256 tokenId
    ) public view returns (address creator, uint256 timestamp) {
        NFTMetaData memory data = nftDetails[tokenId];
        return (data.creator, data.timestamp);
    }

    function tokenURI(
        uint256 tokenId
    ) public view override(ERC721, ERC721URIStorage) returns (string memory) {
        return super.tokenURI(tokenId);
    }

    function supportsInterface(
        bytes4 interfaceId
    ) public view override(ERC721, ERC721URIStorage) returns (bool) {
        return super.supportsInterface(interfaceId);
    }
}
