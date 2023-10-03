import { Component } from '@angular/core';
import { Route, Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {

  username: string = '';
  password: string = '';

  readonly flatObject = [
    {
      "id": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "name": "Object A",
      "parentId": "root",
      "parentName": "root"
    },
    {
      "id": "8183708a-f344-4af1-8222-4791d9b7cf5b",
      "name": "Object C",
      "parentId": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "parentName": "Object A"
    },
    {
      "id": "243b3a5c-f792-4f15-81b2-0dec341eac4f",
      "name": "Object B",
      "parentId": "root",
      "parentName": "root"
    },
    {
      "id": "7d2a3778-fc7e-4eb1-8a32-57eafd23f4bc",
      "name": "Object D",
      "parentId": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "parentName": "Object A"
    },
    {
      "id": "55fbee28-75c1-444f-9d62-9f14026cc3ff",
      "name": "Object E",
      "parentId": "243b3a5c-f792-4f15-81b2-0dec341eac4f",
      "parentName": "Object A"
    }
  ]

  parentChildRelationship: any[] = [];

  constructor(
    private readonly router: Router
  ) {
    this.parentChildRelationship = this.createParentChildRelationship(this.flatObject, 'root');
    console.log(this.parentChildRelationship)
  }

  onSubmit(): void {
    // You can add your authentication logic here
    console.log('Username:', this.username);
    console.log('Password:', this.password);
    // Add authentication logic, e.g., calling an API to validate credentials
    if (this.username.trim() && this.password.trim()) {
      this.router.navigateByUrl(('/home'))
    }
  }


  createParentChildRelationship(data: any[], parentId: string): any[] {
    const result: any[] = [];

    data.forEach(item => {
      if (item.parentId === parentId) {
        const children = this.createParentChildRelationship(data, item.id);
        if (children.length > 0) {
          item.children = children;
        }
        result.push(item);
      }
    });  

    return result;
  }

  showScript1(panel: any) {
    return panel['type']
  }


}
