import {Component, OnInit, ViewChild, ElementRef} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
    selector: 'app-second',
    templateUrl: './second.component.html',
    styleUrls: ['./second.component.scss']
})
export class SecondComponent implements OnInit {
    test;
    head = new HttpHeaders({
        'Access-Control-Allow-Origin': '*'
    });

    options = {headers: this.head};
    apiGetUrl = 'http://localhost:5000/api/getData';
    apiPostUrl = 'http://localhost:5000/api/send';
    x: any;
    loginForm = new FormGroup({
        name: new FormControl(null, [Validators.required]),
        password: new FormControl()
    });

    constructor(private http: HttpClient, private formBuilder: FormBuilder) {
    }

    ngOnInit(): void {
        /*
        this.http.get(this.apiGetUrl).subscribe(
            ok => {
                this.x = ok;
                this.x.list.forEach(function(val): void {
                    console.log(val);
                });
            },
            fil => {
            }
        );
*/
    }

    onSubmit(): void {
        console.log(this.loginForm.value);
        if (this.loginForm.valid) {
            this.http.post(this.apiPostUrl, this.loginForm.value).subscribe(
                ok => {
                    console.log(ok);
                },
                err => {
                    console.log(err);
                }
            );
        } else {
            console.log('Falsche Eingabe');
        }
    }

}
