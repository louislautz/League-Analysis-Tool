import SwiftUI

struct MatchSummary: Identifiable {
    let id = UUID()

    let result: String
    let duration: String
    let queue: String
    let daysAgo: String

    let championName: String
    let championLevel: Int

    let kills: Int
    let deaths: Int
    let assists: Int
    let kda: String

    let killParticipation: String
    let cs: String

    let isWin: Bool
}