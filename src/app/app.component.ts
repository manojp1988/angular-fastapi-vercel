import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';
import { HttpClient, HttpClientModule } from '@angular/common/http';

type Data = {
  message?: string
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'frontend';
  data: Data = {};

  constructor(private http: HttpClient){}

  ngOnInit(){
    this.http.get('/api').subscribe((data: Data) => {
      this.data = data;
    });
  }
}
