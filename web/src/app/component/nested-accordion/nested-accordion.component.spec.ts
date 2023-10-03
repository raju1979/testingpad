import { ComponentFixture, TestBed } from '@angular/core/testing';

import { NestedAccordionComponent } from './nested-accordion.component';

describe('NestedAccordionComponent', () => {
  let component: NestedAccordionComponent;
  let fixture: ComponentFixture<NestedAccordionComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [NestedAccordionComponent]
    });
    fixture = TestBed.createComponent(NestedAccordionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
