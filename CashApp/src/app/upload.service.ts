import {Injectable} from '@angular/core';
import {HttpClient, HttpEvent, HttpErrorResponse, HttpEventType} from '@angular/common/http';
import {map} from 'rxjs/operators';

@Injectable({
    providedIn: 'root'
})
export class UploadService {
    serverUrl = 'http://localhost:5000/api/send';
    constructor(private httpClient: HttpClient) {
    }
    public sendFormdata(formData){
        return this.httpClient.post(this.serverUrl, formData, {
            reportProgress: true,
            observe: 'events'
        });
    }
}
