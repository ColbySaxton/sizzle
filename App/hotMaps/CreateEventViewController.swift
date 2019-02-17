//
//  CreateEventViewController.swift
//  hotMaps
//
//  Created by Colby Saxton on 2/17/19.
//

import UIKit

class CreateEventViewController: UIViewController {


        @IBOutlet weak var RegID: UITextField!
        @IBOutlet weak var busName: UITextField!
        @IBOutlet weak var eventName: UITextField!
        @IBOutlet weak var desc: UITextView!
        
        override func viewDidLoad() {
            super.viewDidLoad()
            
        }
        
        @IBAction func createPushed(_ sender: Any) {
            
            //scrape the information
            
            //pack information into JSON
            
            //send JSON to the server
            
            //reset the fields
            
            RegID.text = ""
            busName.text = ""
            eventName.text = ""
            desc.text = ""
        }
}
