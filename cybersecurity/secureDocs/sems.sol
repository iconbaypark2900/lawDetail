// Specifies the license under which this contract is released.
// SPDX-License-Identifier: MIT

// Sets the compiler version required for this contract.
pragma solidity ^0.8.0;

// Declares the SmartCityLedger contract.
contract SmartCityLedger {
    // Defines a structure for storing environmental data.
    struct EnvironmentalData {
        uint256 timestamp; // Timestamp of the data entry.
        string dataType;   // Type of environmental data (e.g., temperature, humidity).
        uint256 dataValue; // The value of the recorded data.
    }

    // Defines a structure for storing feedback from citizens.
    struct Feedback {
        address citizen;   // Ethereum address of the citizen submitting feedback.
        string message;    // Content of the feedback.
        uint256 timestamp; // Timestamp of the feedback submission.
    }

    // Array to store all environmental data records.
    EnvironmentalData[] public environmentalRecords;
    // Array to store all feedback records from citizens.
    Feedback[] public feedbackRecords;

    // Ethereum address of the city official authorized to perform certain actions.
    address public cityOfficial;

    // Constructor sets the deployer of the contract as the city official.
    constructor() {
        cityOfficial = msg.sender;
    }

    // Modifier to restrict certain functions to the city official only.
    modifier onlyCityOfficial() {
        require(msg.sender == cityOfficial, "Only city officials can perform this action.");
        _; // Continues execution of the function.
    }

    // Stores environmental data. Any account can call this function.
    function storeEnvironmentalData(string memory dataType, uint256 dataValue) public {
        environmentalRecords.push(EnvironmentalData(block.timestamp, dataType, dataValue));
    }

    // Allows citizens to submit feedback. Any account can call this function.
    function submitFeedback(string memory message) public {
        feedbackRecords.push(Feedback(msg.sender, message, block.timestamp));
    }

    // Retrieves the last N environmental records. Accessible to any account.
    function getEnvironmentalRecords(uint256 numberOfRecords) public view returns (EnvironmentalData[] memory) {
        uint256 totalRecords = environmentalRecords.length;
        uint256 resultSize = numberOfRecords > totalRecords ? totalRecords : numberOfRecords;
        EnvironmentalData[] memory results = new EnvironmentalData[](resultSize);

        for (uint256 i = 0; i < resultSize; i++) {
            results[i] = environmentalRecords[totalRecords - resultSize + i];
        }

        return results;
    }

    // Retrieves the last N feedback messages. Restricted to the city official.
    function getFeedback(uint256 numberOfMessages) public view onlyCityOfficial returns (Feedback[] memory) {
        uint256 totalMessages = feedbackRecords.length;
        uint256 resultSize = numberOfMessages > totalMessages ? totalMessages : numberOfMessages;
        Feedback[] memory results = new Feedback[](resultSize);

        for (uint256 i = 0; i < resultSize; i++) {
            results[i] = feedbackRecords[totalMessages - resultSize + i];
        }

        return results;
    }

    // Allows the current city official to delegate their authority to a new official.
    function changeCityOfficial(address newOfficial) public onlyCityOfficial {
        cityOfficial = newOfficial;
    }
}
