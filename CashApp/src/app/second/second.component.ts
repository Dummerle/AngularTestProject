import {Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';

import {CookieService} from 'ngx-cookie-service';

@Component({
    selector: 'app-second',
    templateUrl: './second.component.html',
    styleUrls: ['./second.component.scss']
})
export class SecondComponent implements OnInit {
    test;
    data;
    resp;
    login = false;
    apiGetUrl = 'http://localhost:5000/api/getData';
    apiPostUrl = 'http://localhost:5000/api/send';
    x: any;
    loginForm = new FormGroup({
        password: new FormControl(null, Validators.required)
    });

    constructor(private http: HttpClient, private cookie: CookieService) {
    }

    ngOnInit(): void {
        this.http.get('http://localhost:5000/api/check').subscribe(
            ok => {
                this.login = true;
            }
        );
        this.http.get(this.apiGetUrl).subscribe(
            ok => {
                this.x = ok;
                this.x.list.forEach(function(val): void {
                    // console.log(val);
                });
            },
            fil => {
            }
        );

    }

    onSubmit(): void {
        console.log(this.loginForm.value);
        if (this.loginForm.valid) {
            this.resp = this.http.post(this.apiPostUrl, this.loginForm.value).subscribe(
                ok => {
                    console.log(ok);
                    this.login = true;
                    this.data = ok;
                },
                err => {
                    console.log('FALSCH');
                    this.login = false;
                }
            );

        }
    }
}
