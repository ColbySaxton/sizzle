//
//  ViewController.swift
//  hotMaps
//
//  Created by Colby Saxton on 2/16/19.
//

import UIKit
//import GoogleMaps

class ViewController: UIViewController {

    @IBOutlet weak var leadingSpace: NSLayoutConstraint!
    var menuShow = false
    @IBOutlet weak var menuView: UIView!
    
 //   override func loadView() {
   /*     // Create a GMSCameraPosition that tells the map to display the
        // coordinate -33.86,151.20 at zoom level 6.
        let camera = GMSCameraPosition.camera(withLatitude: -33.86, longitude: 151.20, zoom: 6.0)
        let mapView = GMSMapView.map(withFrame: CGRect.zero, camera: camera)
        view = mapView
        
        // Creates a marker in the center of the map.
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: -33.86, longitude: 151.20)
        marker.title = "Sydney"
        marker.snippet = "Australia"
        marker.map = mapView
 */
//    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        leadingSpace.constant = -225
        menuView.layer.shadowOpacity = 1
        menuView.layer.shadowRadius = 5
    }


    @IBAction func openMenu(_ sender: Any) {
        if(menuShow){
            leadingSpace.constant = -225
            UIView.animate(withDuration: 0.2, animations:{ self.view.layoutIfNeeded()})
            
        }
        else{
            leadingSpace.constant = 0
            UIView.animate(withDuration: 0.2, animations:{ self.view.layoutIfNeeded()})
            
            
        }
        menuShow = !menuShow
    }
}

