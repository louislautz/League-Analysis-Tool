import SwiftUI

struct MatchCard: View {
    let match: MatchSummary

    private var resultColor: Color {
        match.isWin ? .blue : .red
    }

    var body: some View {
        HStack(spacing: 0) {

            Rectangle()
                .fill(resultColor)
                .frame(width: 4)

            VStack(alignment: .leading, spacing: 10) {

                // Top row
                HStack {
                    HStack(spacing: 7) {
                        Text(match.result)
                            .font(.title3)
                            .fontWeight(.bold)
                            .foregroundStyle(resultColor)

                        Text(match.duration)
                            .font(.subheadline)
                            .foregroundStyle(.gray)
                    }

                    Spacer()

                    HStack(spacing: 5) {
                        Text(match.queue)
                            .fontWeight(.semibold)
                            .foregroundStyle(.white)

                        Text("|")
                            .foregroundStyle(.gray)

                        Text(match.daysAgo)
                            .foregroundStyle(.gray)
                    }
                    .font(.caption)
                }

                // Main row
                HStack(alignment: .center, spacing: 12) {

                    // Champion + runes
                    HStack(spacing: 6) {

                        ZStack(alignment: .bottomTrailing) {
                            RoundedRectangle(cornerRadius: 12)
                                .fill(Color.gray.opacity(0.35))
                                .frame(width: 58, height: 58)
                                .overlay {
                                    Text(match.championName)
                                        .font(.caption2)
                                        .foregroundStyle(.white.opacity(0.6))
                                }

                            Text("\(match.championLevel)")
                                .font(.caption2)
                                .fontWeight(.bold)
                                .foregroundStyle(.white)
                                .padding(4)
                                .background(.black.opacity(0.8))
                                .clipShape(Circle())
                        }

                        VStack(spacing: 4) {
                            runeIcon("K")
                            runeIcon("S")
                        }
                    }

                    // KDA
                    VStack(alignment: .leading, spacing: 3) {

                        HStack(spacing: 3) {
                            Text("\(match.kills)")
                                .frame(minWidth: 26, alignment: .trailing)

                            Text("/")
                                .foregroundStyle(.gray)

                            Text("\(match.deaths)")
                                .foregroundStyle(.red)
                                .frame(minWidth: 26)

                            Text("/")
                                .foregroundStyle(.gray)

                            Text("\(match.assists)")
                                .frame(minWidth: 26, alignment: .leading)
                        }
                        .font(.system(size: 22, weight: .bold))
                        .foregroundStyle(.white)
                        .fixedSize()

                        Text(match.kda)
                            .font(.subheadline)
                            .fontWeight(.semibold)
                            .foregroundStyle(.white)
                    }

                    Spacer()

                    // Stats
                    VStack(alignment: .trailing, spacing: 3) {
                        Text(match.killParticipation)
                            .foregroundStyle(.red)

                        Text(match.cs)
                            .foregroundStyle(.white)
                    }
                    .font(.subheadline)
                }

                // Items
                HStack(spacing: 5) {
                    ForEach(0..<7, id: \.self) { index in
                        itemIcon(index)
                    }

                    Spacer()
                }
            }
            .padding(12)
        }
        .background(
            Color(
                red: 0.08,
                green: 0.10,
                blue: 0.11
            )
        )
        .clipShape(RoundedRectangle(cornerRadius: 14))
    }

    private func itemIcon(_ index: Int) -> some View {
        RoundedRectangle(cornerRadius: 6)
            .fill(Color.gray.opacity(0.32))
            .frame(width: 34, height: 34)
    }

    private func runeIcon(_ text: String) -> some View {
        Circle()
            .fill(Color.gray.opacity(0.3))
            .frame(width: 24, height: 24)
            .overlay {
                Text(text)
                    .font(.caption2)
                    .fontWeight(.bold)
                    .foregroundStyle(.white)
            }
    }
}

#Preview {
    VStack(spacing: 10) {
        MatchCard(
            match: MatchSummary(
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
            )
        )

        MatchCard(
            match: MatchSummary(
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
        )
    }
    .padding()
    .background(Color.black)
    .preferredColorScheme(.dark)
}