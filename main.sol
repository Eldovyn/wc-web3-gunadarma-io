// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract TodoList {
    struct Task {
        uint256 id;
        address owner;
        string content;
        bool isCompleted;
    }

    uint256 public taskCount = 0;

    mapping(uint256 => Task) public tasks;

    modifier taskExists(uint256 _id) {
        require(tasks[_id].id != 0, "task tidak di temukan");
        _;
    }

    modifier onlyTaskOwner(uint256 _id) {
        require(tasks[_id].owner == msg.sender, "anda bukan pemilik task ini");
        _;
    }

    function createTask(string calldata _content) public {
        require(bytes(_content).length > 0, "isi task tidak boleh kosong");

        taskCount ++;

        tasks[taskCount] = Task(taskCount, msg.sender, _content, false);
    }

    function getTask(uint256 _id) public view taskExists(_id) onlyTaskOwner(_id) returns (uint256, string memory, bool) {
        Task memory task = tasks[_id];
        return (task.id, task.content, task.isCompleted);
    }

    function updateTaskContent(uint256 _id, string calldata _newContent) public taskExists(_id) onlyTaskOwner(_id) {
        require(bytes(_newContent).length > 0, "isi task tidak boleh kosong");

        tasks[_id].content = _newContent;
    }

    function deleteTasks(uint256 _id) public taskExists(_id) onlyTaskOwner(_id) {
        delete tasks[_id];
    }
}
