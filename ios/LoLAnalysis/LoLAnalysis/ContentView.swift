//
//  ContentView.swift
//  LoLAnalysis
//
//  Created by Louis Lautz on 10.09.26.
//

import SwiftUI

struct ContentView: View {
    let matches: [MatchSummary]

    var body: some View {
        ScrollView {
            VStack(spacing: 10) {
                ForEach(matches) { match in
                    MatchCard(match: match)
                }
            }
            .padding()
        }
    }
}