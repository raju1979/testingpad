import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-nested-accordion',
  templateUrl: './nested-accordion.component.html',
  styleUrls: ['./nested-accordion.component.scss']
})
export class NestedAccordionComponent {
  @Input() accordionData: any[] = [];

  getSettings(panel: any) {
    console.log(panel)
  }

}
