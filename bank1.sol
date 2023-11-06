//SPDX-License-Identifier:Unlicensed
pragma solidity ^ 0.8.0;

contract Bank{
    int balance;
    constructor(){
        balance=0;
    }

    function withdraw(int amount) public{
        if(balance > amount){
            balance=balance-amount;

        }
    }
    function bal() public view returns(int){
        return balance;
    }
    function deposit(int amount) public{
        balance=balance+amount;
    }

}