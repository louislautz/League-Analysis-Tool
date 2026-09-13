//
//  LoLAnalysisApp.swift
//  LoLAnalysis
//
//  Created by Louis Lautz on 10.09.26.
//

import SwiftUI

@main
struct LoLAnalysisApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView(
                matches: [
                    MatchSummary(
                        result: "Win",
                        duration: "26m 32s",
                        queue: "Normal",
                        daysAgo: "12 days ago",
                        championName: "Champ",
                        championLevel: 15,
                        kills: 13,
                        deaths: 5,
                        assists: 6,
                        kda: "3.8:1 KDA",
                        killParticipation: "P/Kill 39%",
                        cs: "CS 170 (6.4)",
                        isWin: true
                    ),
                    MatchSummary(
                        result: "Loss",
                        duration: "31m 43s",
                        queue: "Normal",
                        daysAgo: "13 days ago",
                        championName: "Champ",
                        championLevel: 15,
                        kills: 10,
                        deaths: 6,
                        assists: 9,
                        kda: "3.17:1 KDA",
                        killParticipation: "P/Kill 45%",
                        cs: "CS 193 (6.1)",
                        isWin: false
                    )
                ]
            )
        }
    }
}