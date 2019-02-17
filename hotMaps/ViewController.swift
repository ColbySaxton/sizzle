//
//  ViewController.swift
//  hotMaps
//
//  Created by Colby Saxton on 2/16/19.
//

import UIKit
import GoogleMaps

class ViewController: UIViewController {

    @IBOutlet weak var leadingSpace: NSLayoutConstraint!
    var menuShow = false
    @IBOutlet weak var menuView: UIView!
    
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        
        leadingSpace.constant = -225
        menuView.layer.shadowOpacity = 1
        menuView.layer.shadowRadius = 5
        
        // Create a GMSCameraPosition that tells the map to display the
        // coordinate -33.86,151.20 at zoom level 6.
        let camera = GMSCameraPosition.camera(withLatitude: 41.507050, longitude: -81.609089, zoom: 15.0)
        
        let mapView = GMSMapView.map(withFrame: UIScreen.main.bounds, camera: camera)
        mapView.center = self.view.center
        self.view!.addSubview(mapView)
        //view = mapView
        
        // Creates a marker in the center of the map.
        let marker = GMSMarker()
        marker.position = CLLocationCoordinate2D(latitude: -33.86, longitude: 151.20)
        marker.title = "Sydney"
        marker.snippet = "Australia"
        marker.map = mapView
        
        
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.511130, longitude: -81.602635), title: "happyDog", desc: "fools gold", venueType: 1)
        
         addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.509197, longitude: -81.605424), title: "Sports Bar: Corner Alley" , desc: "Location: 402 Euclid Ave, Cleveland, OH 44114 \nTime: 9:00pm - 2:00am \nDescription: Come join us in the heart of downtown as we watch the final regular season game for the Cleveland Cavaliers! Defend the LAND!", venueType: 1)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.508736, longitude: -81.604605), title: "Hotel Bar: The Vault", desc: "Location: 2017 E 9th St, Cleveland, OH 44115\nTime: 8:00pm - 2:30am \nDescription: Travel back in time and experience the glamor and luxury of a classic 1800s Cleveland bank. Surround yourself in elegance, history, and incredible hand-crafted cocktails.", venueType: 2)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.507441, longitude: -81.608250), title: "Music: Drag Queen Show @ The Jolly Scholar", desc: "Location: Thwing Center, 11111 Euclid Ave, Cleveland, OH 44106\nTime: 8:00pm - 10:00pm\nDescription: Catch Rupaul’s, “A Drag Queen’s Christmas” with discounted prices exclusively on Habanero! ", venueType: 5)
        addMarker(map: mapView, position: CLLocationCoordinate2D(latitude: 41.500801    , longitude: -81.592810), title: "Specialty: Fairmount Bar", desc: "Location: 2448 Fairmount Blvd, Cleveland, OH 44106\nTime: 8:00pm - 1:30am\nDescription: Enjoy Cleveland’s best made to order drinks, with over fifty beers on tap. Immerse yourself in this young and upcoming area in Cleveland Heights!", venueType: 8)
        
    }


    @IBAction func openMenu(_ sender: Any) {
        self.view.bringSubviewToFront(menuView)
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
    
    private func addMarker(map: GMSMapView, position: CLLocationCoordinate2D, title: String, desc: String, venueType: Int){

        
        
        var ic : UIImage
        let marker = GMSMarker(position: position)

        switch(venueType){
            //load different icon for  each venue (custom markers)
        case 1:
            ic = GMSMarker.markerImage(with: UIColor.blue)
        case 2:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.0, green: 0.0, blue: 0.75, alpha: 1.0))
        case 3:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.0, green: 0.0, blue: 0.5, alpha: 1.0))
        case 4:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.0, green: 0.0, blue: 0.25, alpha: 1.0))
        case 5:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.25, green: 0.0, blue: 0.0, alpha: 1.0))
        case 6:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.5, green: 0.0, blue: 0.0, alpha: 1.0))
        case 7:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 0.75, green: 0.0, blue: 0.0, alpha: 1.0))
        case 8:
            ic = GMSMarker.markerImage(with: UIColor.init(red: 1.0, green: 0.0, blue: 0.0, alpha: 1.0))
        default:
            //todo error log here for a bad venue type
            ic = GMSMarker.markerImage(with: UIColor.red)
        }
        

        
        marker.icon = ic;
        marker.title = title
        marker.snippet = desc
        marker.map = map
        
        
    }
}

