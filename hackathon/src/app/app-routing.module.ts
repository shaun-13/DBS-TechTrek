import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './login/login.component';
import { HomeComponent } from './home/home.component';
import { TransferComponent } from './transfer/transfer.component';

const routes: Routes = [{ path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'transfer', component: TransferComponent },
  { path: '', redirectTo: 'login', pathMatch: 'full' }];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
