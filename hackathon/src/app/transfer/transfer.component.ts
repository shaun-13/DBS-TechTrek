import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-transfer',
  templateUrl: './transfer.component.html',
  styleUrls: ['./transfer.component.css']
})
export class TransferComponent implements OnInit {
  payee?: string;
  amount?: string;
  constructor() { }

  ngOnInit(): void {
  }

  addTodo(){
    console.log(this.payee);
    console.log(this.amount);
  }

}
