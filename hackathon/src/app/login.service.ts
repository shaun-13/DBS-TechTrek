import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, retry } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LoginService {

  constructor(private http: HttpClient) { }
  login() {
  this.http.post<any>("http://127.0.0.1:5002/login", {
    "username": "Group8",
    "password": "DeZeYBsY1CRcacw"
}).subscribe((e) => console.log(e));
}
}
