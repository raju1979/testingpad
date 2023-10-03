import { Component, Input, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.scss']
})
export class HomeComponent implements OnInit {

  readonly flatObject = [
    {
      "id": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "displayName": "Object A",
      "parentId": "xaae",
      "parentName": "root",
      "type": "folder",
      route: 'orlando',
      "notes": [
        "I am a note for folder Object A"
      ]
    },
    {
      "id": "8183708a-f344-4af1-8222-4791d9b7cf5b",
      "displayName": "Object C",
      "parentId": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "parentName": "Object A",
      "type": "folder",
      route: 'orlando',
      "notes": [
        "I am a note for folder Object C"
      ]
    },
    {
      "id": "243b3a5c-f792-4f15-81b2-0dec341eac4f",
      "displayName": "Object B",
      "parentId": "xaae",
      "parentName": "root",
      "type": "folder",
      route: 'orlando',
    },
    {
      "id": "7d2a3778-fc7e-4eb1-8a32-57eafd23f4bc",
      "displayName": "Object D",
      "parentId": "84e37af0-2141-4206-a58f-98e9737d50ac",
      "parentName": "Object A",
      "type": "script",
      route: 'orlando',
    },
    {
      "id": "55fbee28-75c1-444f-9d62-9f14026cc3ff",
      "displayName": "Object E",
      "parentId": "243b3a5c-f792-4f15-81b2-0dec341eac4f",
      "parentName": "Object B",
      "type": "folder",
      route: 'orlando',
    },
    {
      "id": "55fbee28-75c1-444f-9d62-9f14026cc3f4",
      "displayName": "Object F",
      "parentId": "55fbee28-75c1-444f-9d62-9f14026cc3ff",
      "parentName": "Object E",
      "type": "script",
      route: 'orlando',
    }
  ]


  panels: any[] = [];

  parentChildRelationship: any[] = [];


  constructor() {

  }

  ngOnInit() {
    const tempPanelArray: any[] = [];
    this.parentChildRelationship = this.createParentChildRelationship(this.flatObject, 'xaae');
    console.log(this.parentChildRelationship)
    this.panels = [...this.parentChildRelationship];
  }

  createParentChildRelationship(data: any[], parentId: string): any[] {
    const result: any[] = [];

    data.forEach(item => {
      if (item.parentId === parentId) {
        const childPanel = this.createParentChildRelationship(data, item.id);
        item['active'] = true;
          item['disabled'] = false;
        if (childPanel.length > 0) {
          item['active'] = true;
          item['disabled'] = false;
          item.childPanel = childPanel;
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
