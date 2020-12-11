import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  username: string;
  password: string;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit(): void {
  }
login(){
  console.log(this.username);
  console.log(this.password);

}
}