import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-transfer',
  templateUrl: './transfer.component.html',
  styleUrls: ['./transfer.component.css']
})
export class TransferComponent implements OnInit {

  //update account balance api params
  custID?: number;
  updateAmount?: number;

  payeeID?: string;
  amount?: number;
  dateTime?: Date;
  expensesCat?: string;
  eGift?: Boolean;
  message?: String;

  constructor() { }

  ngOnInit(): void {
  }

  addTodo(){
    console.log(this.payeeID);
    console.log(this.amount);
  }

}
